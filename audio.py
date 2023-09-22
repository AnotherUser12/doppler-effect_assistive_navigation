import numpy as np
import pyaudio
import threading

# Function to generate stereo audio data
def generate_beep(doppler_frequency, audio_frequency=440, volume=0.5, sample_rate=44100):
    duration = 2/(2*doppler_frequency) #seconds
    print("duration", duration)
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    
    sound = volume * np.sin(2 * np.pi * audio_frequency * t)
    no_sound = np.zeros_like(sound)
    
    return np.concatenate((sound, no_sound))

def generate_stereo_beep(isLeft, doppler_frequency, audio_frequency=440):
    print('stereo beep called')
    positive_channel = generate_beep(doppler_frequency, audio_frequency=audio_frequency)
    neutral_channel = np.zeros_like(positive_channel)

    if isLeft:
        left_channel=positive_channel
        right_channel=neutral_channel
    else:
        left_channel=neutral_channel
        right_channel=positive_channel
    
    stereo_beep = np.column_stack((left_channel, right_channel))
    return stereo_beep.astype(np.float32)

def play_stereo_audio(stereo_audio, event=None, sample_rate=44100):
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

        if event:
            event.set()

def async_play_stereo_audio(stereo_audio):
    event = threading.Event()
    # Create a thread for playing stereo audio asynchronously
    audio_thread = threading.Thread(target=play_stereo_audio, args=(stereo_audio, event))

    # Start the audio thread
    audio_thread.start()
    return event