import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment
from io import BytesIO

def numpy_array_to_mp3(audio_array, sample_rate, file_name):
    # Convert numpy array to a WAV file in memory
    wav_io = BytesIO()
    write(wav_io, sample_rate, audio_array)
    wav_io.seek(0)
    
    # Convert WAV file in memory to MP3
    audio_segment = AudioSegment.from_wav(wav_io)
    audio_segment.export(file_name, format="mp3")

def generate_sine_wave(frequency, duration, sample_rate, volume_factor=0.5):
    num_samples = duration * sample_rate
    t = np.arange(num_samples) / sample_rate
    sine_wave = volume_factor * np.sin(2 * np.pi * frequency * t)
    return (sine_wave * 32767).astype(np.int16)

def generate_square_wave(frequency, duration, sample_rate, volume_factor=0.5):
    num_samples = duration * sample_rate
    t = np.arange(num_samples) / sample_rate
    square_wave = volume_factor * np.sign(np.sin(2 * np.pi * frequency * t))
    return (square_wave * 32767).astype(np.int16)

def generate_triangle_wave(frequency, duration, sample_rate, volume_factor=0.5):
    num_samples = duration * sample_rate
    t = np.arange(num_samples) / sample_rate
    triangle_wave = volume_factor * (2 * np.abs(2 * (t * frequency - np.floor(t * frequency + 0.5))) - 1)
    return (triangle_wave * 32767).astype(np.int16)

def generate_sawtooth_wave(frequency, duration, sample_rate, volume_factor=0.5):
    num_samples = duration * sample_rate
    t = np.arange(num_samples) / sample_rate
    sawtooth_wave = volume_factor * (1 - np.mod(t * frequency, 1))
    return (sawtooth_wave * 32767).astype(np.int16)

# Example usage
frequency = 440  # A4 note
duration = 5  # 5 seconds
sample_rate = 44100  # CD quality
volume_factor = 0.3  # Reduce volume to 30% of full scale

# Generate and save as MP3
numpy_array_to_mp3(generate_sine_wave(frequency, duration, sample_rate, volume_factor), sample_rate, 'sine_wave.mp3')
numpy_array_to_mp3(generate_square_wave(frequency, duration, sample_rate, volume_factor), sample_rate, 'square_wave.mp3')
numpy_array_to_mp3(generate_triangle_wave(frequency, duration, sample_rate, volume_factor), sample_rate, 'triangle_wave.mp3')
numpy_array_to_mp3(generate_sawtooth_wave(frequency, duration, sample_rate, volume_factor), sample_rate, 'sawtooth_wave.mp3')
