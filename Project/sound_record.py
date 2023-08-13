import os
import sounddevice as sd
import numpy as np
from datetime import datetime

# Constants for audio settings
SAMPLE_RATE = 44100  # Sample rate in Hz
RECORD_DURATION = 10  # Recording duration in seconds

# Global variable to indicate whether to continue recording
recording = False

def audio_callback(indata, frames, time, status):
    global recording
    if status:
        print("Error:", status)
    if recording:
        # Check if the audio contains significant sound (non-silence)
        if np.max(np.abs(indata)) > 0.01:
            recording = False
            print("Recording stopped")
            # Create the "audio" directory if it doesn't exist
            if not os.path.exists("audio"):
                os.makedirs("audio")
            # Get current date and time
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
            # Save the recorded audio to a WAV file with the timestamp as the name within the "audio" directory
            audio_filename = os.path.join("audio", f"recorded_audio_{timestamp}.wav")
            sd.write(audio_filename, indata, SAMPLE_RATE)
            print(f"Recording saved as {audio_filename}")

def start_recording():
    global recording
    recording = True
    print("Recording started")

with sd.InputStream(callback=audio_callback, channels=1, samplerate=SAMPLE_RATE):
    print("Listening for user speech...")
    try:
        while True:
            input("Press Enter to start recording or Ctrl+C to exit...\n")
            start_recording()
    except KeyboardInterrupt:
        pass

