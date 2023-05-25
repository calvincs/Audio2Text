import pyaudio
import numpy as np
from scipy.io.wavfile import write
import time
import whisper
import pygame
import logging

class Audio2Text:
    FORMAT = pyaudio.paInt16  # Audio format
    CHANNELS = 1  # Mono audio
    RATE = 44100  # Sample rate
    CHUNK = 1024  # Frames per buffer


    def __init__(self, threshold: int, silence_limit: int, recording_limit: int, filename: str, keyword: str, model: str = "base.en"):
        """
        Initialize the AudioRecorder class.

        :param threshold: The threshold value for starting the recording
        :param silence_limit: Silence limit in seconds
        :param recording_limit: Maximum recording length
        :param filename: Output filename
        :param keyword: The word to listen for
        :param model: The whisper model to use
        """
        # Initialize variables
        self.threshold = threshold
        self.silence_limit = silence_limit
        self.recording_limit = recording_limit
        self.filename = filename
        self.keyword = keyword.lower()
        self.audio = pyaudio.PyAudio()
        self.model = whisper.load_model(model)
        # Pygame initialization for playing sound
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.load("ding.mp3")
        # Get the logger
        self.logger = logging.getLogger("Audio2Text")


    def start_recording(self):
        """
        Start recording audio from the microphone.

        :return: None
        """
        frames = []
        silence_frames = 0
        total_frames = 0
        recording_started = False
        stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)

        try:
            self.logger.info("Listening...")
            while True:
                # Read audio data
                try:
                    data = stream.read(self.CHUNK)
                except IOError:
                    self.logger.warning("Stream overflow: skipping this chunk of data.")
                    continue
                # Convert data to numpy array
                npdata = np.frombuffer(data, dtype=np.int16)
                np_mean = np.abs(npdata).mean()
                loud_enough = np_mean > self.threshold
                # If loud enough or recording started, add to frames
                if loud_enough:
                    frames.append(npdata)
                    silence_frames = 0
                    if not recording_started:
                        recording_started = True
                elif recording_started:
                    frames.append(npdata)
                    silence_frames += 1
                    # Stop recording if there is no audio for more than silence_limit seconds
                    if silence_frames > self.silence_limit * self.RATE / self.CHUNK:
                        self.logger.info("Reached silence limit. Stopping.\n")
                        break
                else:
                    # Decrease the threshold by 0.01% every 150 frames 
                    if np_mean < self.threshold and self.threshold > 150:
                        self.threshold -= (self.threshold * 0.0001)
                if self.recording_limit > 0:
                    # Stop recording after recording_limit seconds
                    if recording_started and total_frames >= self.RATE / self.CHUNK * self.recording_limit:
                        self.logger.info("Reached recording time limit. Stopping.")
                        break

                if recording_started:
                    total_frames += 1
        finally:
            stream.stop_stream()
            stream.close()

        self.logger.info("Finished recording.")

        # Save the recorded data as a WAV file (temporarily)
        if len(frames) > 0:
            frames = np.concatenate(frames)
            write(self.filename, self.RATE, frames)
            self.logger.info("Saved audio to: %s", self.filename)
            text_output = self.speech_to_text(self.filename)

            cleaned_text = text_output.lower().strip()
            if self.keyword in cleaned_text:
                self.logger.info("keyword detected")
                pygame.mixer.music.play()
            
            # Return the captured text
            return text_output


    def speech_to_text(self, filename):
        """
            Speech to text using the whisper library.

            :param filename: The filename of the audio file to transcribe
            :return: The transcribed text
        """
        result = self.model.transcribe(filename)
        self.logger.info(f"What we heard: {result['text']}\n\n")
        return result['text'].lower()
