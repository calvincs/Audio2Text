# Audio2Text - A voice-triggered keyword logger

## Overview
Audio2Text is a Python utility that continuously listens to audio input, recording when a specified sound threshold is reached and stopping after a period of silence or a set recording limit. This utility includes a keyword recognition feature that triggers a notification sound and logs the event when a specified keyword is detected in the recorded speech.

## Who
This software is designed for researchers, developers, and anyone interested in audio processing, voice activity detection (VAD), or keyword recognition in live audio streams.

## What
Audio2Text uses `pyaudio` for audio input, `numpy` and `scipy` for audio processing, and the `whisper` library for speech recognition. A `pygame` sound is triggered when a designated keyword is detected. It includes a logger to keep track of the system status and the detected events.

## Why
Audio2Text is useful in a variety of contexts, from home automation (e.g., a voice-triggered light switch) to live transcription services, or even security systems that react to specific keywords. This utility provides an easy-to-use foundation for such applications.

## How to use

1. Clone the repository:

   ```bash
   git clone https://github.com/calvincs/audio2text.git
   cd audio2text
   ```

2. Run the install script to install dependencies:

   ```bash
   ./dependency-install.sh
   ```

3. Activate the python environment:

   ```bash
   source a2text/bin/activate
   ```

4. Import the module and create an Audio2Text instance:

   ```python
   import logging
   from audio2text import Audio2Text

   # Set the logging level to INFO to display the output
   logging.basicConfig(level=logging.INFO)

   # Initialize an instance of Audio2Text
   audio2text = Audio2Text(
       threshold=500,
       silence_limit=1,
       recording_limit=10,
       filename="output.wav",
       keyword="hello",
       model="base.en"
   )
   ```

5. Start recording:

   ```python
   text_output = audio2text.start_recording()

   print(f"Transcribed text: {text_output}")
   ```
## Argument Details

The Audio2Text class takes a number of arguments that can be used to customize its behavior.

By adjusting these parameters, you can customize the Audio2Text class to suit your specific needs. For example, you might want to use a higher threshold if you're in a noisy environment, or a longer silence limit if you're transcribing speech with long pauses. 

### `threshold`

The `threshold` parameter determines the minimum loudness level required for the audio input to be considered "loud enough" and for the recording to start. The loudness of the audio input is measured as the mean absolute value of the audio data. If the loudness of the audio input exceeds the threshold, the recording starts.

- Type: `int`
- Default value: No default value; must be specified when initializing the Audio2Text class.

   ```python
   audio2text = Audio2Text(threshold=500, ...)
   ```

### `silence_limit`

The `silence_limit` parameter specifies the maximum duration (in seconds) of silence allowed before the recording stops. If the loudness of the audio input falls below the threshold for longer than the silence limit, the recording stops.

- Type: `int`
- Default value: No default value; must be specified when initializing the Audio2Text class.

   ```python
   audio2text = Audio2Text(silence_limit=1, ...)
   ```

### `recording_limit`

The `recording_limit` parameter specifies the maximum duration (in seconds) of the recording. If the recording reaches this limit, it stops even if the audio input is still loud enough.

- Type: `int`
- Default value: No default value; must be specified when initializing the Audio2Text class.

   ```python
   audio2text = Audio2Text(recording_limit=10, ...)
   ```

### `filename`

The `filename` parameter specifies the name of the temporary WAV file where the recorded audio data is saved before it's transcribed.

- Type: `str`
- Default value: No default value; must be specified when initializing the Audio2Text class.

   ```python
   audio2text = Audio2Text(filename="output.wav", ...)
   ```

### `keyword`

The `keyword` parameter specifies the word that the Audio2Text class listens for. If this word is detected in the transcribed text, a sound is played and a message is logged.

- Type: `str`
- Default value: No default value; must be specified when initializing the Audio2Text class.

   ```python
   audio2text = Audio2Text(keyword="hello", ...)
   ```

### `model`

The `model` parameter specifies the whisper model to use for speech recognition. By default, the "base.en" model is used.

You might also want to use a different whisper model if you're working with a language other than English or a specific accent.

- Type: `str`
- Default value: "base.en"

   ```python
   audio2text = Audio2Text(model="base.en", ...)
   ```


## Logging
The logger outputs messages to the console when it starts and stops listening, when the silence limit or the recording limit is reached, when the audio is saved to a file, and when a keyword is detected in the transcribed text. To see these messages, set the logging level to INFO when initializing the logger.

## Notes
The audio file saved by this utility is a temporary file that serves as input to the speech-to-text process. Be mindful of the amount of storage space available if you're planning to use this utility for long or frequent recordings. The logger's output could be redirected to a file to keep a record of the detected events.

The Audio2Text class is fully customizable. You can easily modify it to suit your specific needs, for instance, changing the model used for speech recognition, adjusting the sound threshold and silence limit, or implementing additional features such as multiple keyword recognition or different notification sounds for different keywords.

You can find more information on Whispers models and options: [Openai-Whisper](https://pypi.org/project/openai-whisper/)

## Dependencies
This utility relies on several libraries:

- `pyaudio`: for recording audio from the microphone
- `numpy`: for processing audio data
- `scipy.io.wavfile`: for saving audio data as a WAV file
- `whisper`: for speech recognition
- `pygame`: for playing a sound when a keyword is detected

These dependencies can be installed by running the provided `dependency-install.sh` script.

## Considerations
Keep in mind that the performance of Audio2Text might be impacted by the quality of the microphone, the loudness of the input speech, and the level of background noise. You might need to adjust the threshold parameter depending on your setup.

The whisper library's model can be replaced with another model according to your needs. If you wish to recognize a language other than English or a specific accent, consider using a different model.

Diffrent whisper models will respond differently depending on the quality of your input.

## License
This project is open source, under the terms of the [MIT License](https://opensource.org/licenses/MIT). This means that you can use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, under the given terms.

## Contributing
If you would like to contribute to the development of Audio2Text, please follow these steps:

1. Fork the project.
2. Create a new branch for your feature.
3. Commit your changes to the new branch.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

## Support
If you encounter any issues while using Audio2Text, please open an issue on the [Github repository](https://github.com/calvincs/audio2text/issues). We'll do our best to help.

## Future Work
We plan on enhancing the Audio2Text utility with more features such as multiple keyword recognition, different notification sounds for different keywords, and an option to persist audio recordings. Stay tuned!

## Contact
For further inquiries or if you'd like to get involved, reach out via [Github](https://github.com/calvincs). We'd love to hear from you!
