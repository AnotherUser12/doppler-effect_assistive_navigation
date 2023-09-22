import numpy as np
import pyaudio
import threading

# Function to generate stereo audio data
def generate_stereo_audio(left_frequency, right_frequency, duration_ms, volume=0.5, sample_rate=44100):
    t = np.linspace(0,  1, int(sample_rate * 1), endpoint=False)
    
    left_channel = volume * np.sin(2 * np.pi * left_frequency * t)
    right_channel = np.zeros_like(left_channel)
    
    stereo_audio = np.column_stack((left_channel, right_channel))
    
    return stereo_audio.astype(np.float32)

# Function to play stereo audio asynchronously
def play_stereo_audio(stereo_audio, sample_rate=44100):
    p = pyaudio.PyAudio()

    stream = p.open(
        format=pyaudio.paFloat32,
        channels=2,  # Stereo audio
        rate=sample_rate,
        output=True
    )

    stream.start_stream()
    stream.write(stereo_audio.tobytes())
    stream.stop_stream()
    stream.close()

    p.terminate()

# Create stereo audio data
left_frequency = 440  # Frequency for the left channel (e.g., 440 Hz)
right_frequency = 880  # Frequency for the right channel (e.g., 880 Hz)
stereo_audio = generate_stereo_audio(left_frequency, right_frequency, 5000)  # 5 seconds

# Create a thread for playing stereo audio asynchronously
audio_thread = threading.Thread(target=play_stereo_audio, args=(stereo_audio,))

# Start the audio thread
audio_thread.start()

# The main script continues running while stereo audio is played asynchronously
print("Script continues running while stereo audio is playing.")