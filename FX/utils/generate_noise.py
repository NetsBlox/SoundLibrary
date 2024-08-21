import numpy as np
from scipy.io.wavfile import write
from scipy.signal import lfilter
from pydub import AudioSegment
from io import BytesIO

# Parameters
duration = 5  # in seconds
sample_rate = 44100  # in Hz (standard for audio CDs)
amplitude = 32767  # max amplitude for 16-bit audio
frequency = 440  # A4 note

def numpy_array_to_mp3(audio_array, sample_rate, file_name):
    # Convert numpy array to a WAV file in memory
    wav_io = BytesIO()
    write(wav_io, sample_rate, audio_array)
    wav_io.seek(0)
    
    # Convert WAV file in memory to MP3
    audio_segment = AudioSegment.from_wav(wav_io)
    audio_segment.export(file_name, format="mp3")

# Generate white noise
def generate_white_noise(duration, sample_rate):
    num_samples = duration * sample_rate
    white_noise = np.random.uniform(-1, 1, num_samples)
    return (white_noise * amplitude).astype(np.int16)

# Generate brown noise (also known as red noise)
def generate_brown_noise(duration, sample_rate):
    num_samples = duration * sample_rate
    white_noise = np.random.uniform(-1, 1, num_samples)
    # Integrate white noise to get brown noise
    brown_noise = np.cumsum(white_noise)
    brown_noise -= np.mean(brown_noise)
    brown_noise = np.clip(brown_noise / np.max(np.abs(brown_noise)), -1, 1)
    return (brown_noise * amplitude).astype(np.int16)

# Generate pink noise
def generate_pink_noise(duration, sample_rate):
    num_samples = duration * sample_rate
    white_noise = np.random.randn(num_samples)
    # Apply filter to get pink noise
    b = [0.02109238, 0.07113478, 0.68873558, 1.0, 0.68873558, 0.07113478, 0.02109238]
    a = [1.0, -1.36928060, 1.27583428, -0.38670807]
    pink_noise = lfilter(b, a, white_noise)
    pink_noise -= np.mean(pink_noise)
    pink_noise = np.clip(pink_noise / np.max(np.abs(pink_noise)), -1, 1)
    return (pink_noise * amplitude).astype(np.int16)



# Save to WAV files
numpy_array_to_mp3(generate_white_noise(duration, sample_rate),sample_rate,'white_noise.mp3')
numpy_array_to_mp3(generate_brown_noise(duration, sample_rate),sample_rate,'brown_noise.mp3')
numpy_array_to_mp3(generate_pink_noise(duration, sample_rate),sample_rate,'pink_noise.mp3')


