import numpy as np
import sounddevice as sd

# Define the audio properties
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration of the audio in seconds

# Generate some sample stereo audio data using NumPy
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
left_channel = np.sin(2 * np.pi * 440 * t)  # 440 Hz sine wave for left channel
right_channel =  np.zeros_like(left_channel) # 880 Hz sine wave for right channel

# Combine the left and right channels into stereo audio
stereo_audio = np.column_stack((left_channel, right_channel))

# Scale the audio to the appropriate range (-1 to 1)
stereo_audio = stereo_audio.astype(np.float32)

# Define a callback function to stream the audio asynchronously
def callback(outdata, frames, time, status):
    if status:
        print(status, flush=True)
    outdata[:] = stereo_audio[:frames]

# Open a sound device for playback
with sd.OutputStream(samplerate=sample_rate, channels=2, callback=callback):
    sd.sleep(int(duration * 1000))  # Sleep for the duration of the audio

# The script will continue running while the audio is played asynchronously
print("Script continues running while audio is playing.")