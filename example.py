import logging
import time
from audio2text import Audio2Text


if __name__ == "__main__":
    # Set up logging
    logger = logging.getLogger("Audio2Text")
    logger.setLevel(logging.INFO)  # Log all messages of level INFO and above

    ch = logging.StreamHandler()  # Create console handler
    ch.setLevel(logging.INFO)  # Set level of console handler

    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(ch)

    recorder = Audio2Text(200, 2, 180, "output.wav", "Hey computer")

    try:
        while True:
            text_output = recorder.start_recording()
            print(text_output)

            time.sleep(0.25)
    except Exception as e:
        print(e)
    finally:
        recorder.audio.terminate()
