import numpy as np
from pydub import AudioSegment
from pydub.playback import play

# Define the audio properties
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration of the audio in seconds

# Generate some sample stereo audio data using NumPy
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
left_channel = np.sin(2 * np.pi * 440 * t)  # 440 Hz sine wave for left channel
right_channel = np.zeros_like(left_channel)

# Combine the left and right channels into stereo audio
stereo_audio = np.column_stack((left_channel, right_channel))

# Scale the audio to the appropriate range (-32768 to 32767 for 16-bit PCM)
stereo_audio = np.int16(stereo_audio * 32767)

# Create a PyDub AudioSegment from the stereo audio data
audio = AudioSegment(
    stereo_audio.tobytes(),
    frame_rate=sample_rate,
    sample_width=stereo_audio.dtype.itemsize,
    channels=2  # Stereo audio
)

# Play the generated audio
play(audio, block=False)
print('hello')

t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
right_channel = np.sin(2 * np.pi * 440 * t)  # 440 Hz sine wave for left channel
left_channel = np.zeros_like(left_channel)

# Combine the left and right channels into stereo audio
stereo_audio = np.column_stack((left_channel, right_channel))

# Scale the audio to the appropriate range (-32768 to 32767 for 16-bit PCM)
stereo_audio = np.int16(stereo_audio * 32767)

# Create a PyDub AudioSegment from the stereo audio data
audio = AudioSegment(
    stereo_audio.tobytes(),
    frame_rate=sample_rate,
    sample_width=stereo_audio.dtype.itemsize,
    channels=2  # Stereo audio
)

# Play the generated audio
play(audio)