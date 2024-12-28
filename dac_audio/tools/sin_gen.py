import numpy as np

# Parameters
frequency = 500  # Frequency of the sine wave in Hz
duration = 5      # Duration of the sine wave in seconds
sampling_rate = 44100  # Sampling rate in Hz

# Generate time values
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate sine wave
sine_wave = np.sin(2 * np.pi * frequency * t)

# Convert to 8-bit PCM format
sine_wave_pcm = np.uint8((sine_wave + 1) * 127.5)  # Scale to 0-255 range

# Save to a header file
with open('sin500Hz.h', 'w') as f:
    f.write('#ifndef SIN500HZ_H\n')
    f.write('#define SIN500HZ_H\n\n')
    f.write('const uint8_t audio_table[] = {\n')
    for i, sample in enumerate(sine_wave_pcm):
        if i % 12 == 0:
            f.write('\n    ')
        f.write(f'0x{sample:02X}, ')
    f.write('\n};\n\n')
    f.write('#endif // SIN500HZ_H\n')

print("Sine wave table generated and saved to sin500Hz.h")