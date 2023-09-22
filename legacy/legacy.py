import numpy as np
import math
import pyaudio
import threading
import time

# Global variables for audio playback control
stop_playback = False
audio_thread = None

def interchange_numpy_arrays(array1, array2, interval):
    interval = int(interval)
    if interval < 1:
        interval = 1  # Ensure interval is at least 1 to avoid issues

    result = []
    for i in range(0, len(array1), interval):
        result.extend(array1[i:i+interval])
        result.extend(array2[i:i+interval])
    return np.array(result)

def play_audio(audio_data, sample_rate):
    global stop_playback
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=2,
                    rate=sample_rate,
                    output=True)
    for chunk in audio_data:
        if stop_playback:
            break
        stream.write(chunk.tobytes())
    stream.stop_stream()
    stream.close()
    p.terminate()

def signal_turn(isLeft, audio_frequency, doppler_frequency):
    global audio_thread
    global stop_playback

    # Stop the previous playback, if any
    stop_playback = True
    if audio_thread:
        audio_thread.join()
    stop_playback = False

    sample_rate = 44100
    duration = 1
    volume = 0.5

    t = np.linspace(0, duration, int(sample_rate * duration))
    positive_signal = volume * np.sin(2 * math.pi * audio_frequency * t)
    neutral_signal = np.zeros_like(positive_signal)

    positive_signal = interchange_numpy_arrays(positive_signal, neutral_signal, sample_rate / doppler_frequency)
    neutral_signal = np.concatenate((neutral_signal, neutral_signal))

    if isLeft:
        left_signal = positive_signal
        right_signal = neutral_signal
    else:
        left_signal = neutral_signal
        right_signal = positive_signal

    audio_data = np.column_stack((left_signal, right_signal))

    # Play audio in a separate thread
    audio_thread = threading.Thread(target=play_audio, args=(audio_data, sample_rate))
    audio_thread.start()

# Call the function to play audio in a separate thread
signal_turn(True, 8000, 1)

# Sleep for a while to allow the first sound to play (you can remove this if not needed)
time.sleep(2)

# Play the second sound asynchronously
signal_turn(True, 6000, 3)

# Sleep for a while to allow the second sound to play (you can remove this if not needed)
time.sleep(2)

# Stop the playback of the second sound
stop_playback = True
if audio_thread:
    audio_thread.join()

# Play a new sound
signal_turn(True, 3000, 2)
