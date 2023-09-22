import numpy as np
import math
import sounddevice as sd


def interchange_numpy_arrays(array1, array2, interval):
    interval=int(interval)
    if interval < 1:
        interval = 1  # Ensure interval is at least 1 to avoid issues

    result = []
    for i in range(0, len(array1), interval):
        result.extend(array1[i:i+interval])
        result.extend(array2[i:i+interval])
    return np.array(result)

def signal_turn(isLeft, audio_frequency, doppler_frequency):
    sample_rate = 44100
    duration = 1
    volume = 0.5
    num_samples = int(sample_rate * duration)  # Convert to integer

    t = np.linspace(0, duration, num_samples)
    positive_signal = volume * np.sin(2 * math.pi * audio_frequency * t)
    neutral_signal = np.zeros_like(positive_signal)

    positive_signal = interchange_numpy_arrays(positive_signal, neutral_signal, sample_rate/doppler_frequency)

    # Fix the typo here
    neutral_signal = np.concatenate((neutral_signal, neutral_signal))
    print(positive_signal)
    print(positive_signal.shape)
    print(neutral_signal.shape)

    if isLeft:
        left_signal = positive_signal
        right_signal = neutral_signal
    else:
        left_signal = neutral_signal
        right_signal = positive_signal

    audio_data = np.column_stack((left_signal, right_signal))

    sd.play(audio_data, sample_rate)
    sd.wait()

signal_turn(True, 2000, 1)
signal_turn(True, 2000, 3)
