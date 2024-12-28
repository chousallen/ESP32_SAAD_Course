import os
import wave
import numpy as np

def convert_wav_to_header(wav_filename):
    with wave.open(wav_filename, 'rb') as wav_file:
        params = wav_file.getparams()
        n_channels, sampwidth, framerate, n_frames, comptype, compname = params[:6]
        
        frames = wav_file.readframes(n_frames)
        
        if sampwidth == 1:
            samples = np.frombuffer(frames, dtype=np.uint8)
        else:
            # Convert to 8-bit
            if sampwidth == 2:
                samples = np.frombuffer(frames, dtype=np.int16)
            elif sampwidth == 4:
                samples = np.frombuffer(frames, dtype=np.int32)
            else:
                raise ValueError("Unsupported sample width")
            
            # Convert to float32 to avoid overflow
            samples = samples.astype(np.float32)
            
            # Normalize to range 0-255
            samples = ((samples - samples.min()) / (samples.max() - samples.min()) * 255).astype(np.uint8)
        
        header_filename = os.path.splitext(wav_filename)[0] + '.h'
        with open(header_filename, 'w') as header_file:
            header_file.write(f'#ifndef {os.path.splitext(wav_filename)[0].upper()}_H\n')
            header_file.write(f'#define {os.path.splitext(wav_filename)[0].upper()}_H\n\n')
            header_file.write(f'const uint8_t {os.path.splitext(wav_filename)[0]}_data[] = {{\n')
            for i, sample in enumerate(samples):
                if i % 12 == 0:
                    header_file.write('\n    ')
                header_file.write(f'0x{sample:02X}, ')
            header_file.write('\n};\n\n')
            header_file.write(f'#endif // {os.path.splitext(wav_filename)[0].upper()}_H\n')

def main():
    for filename in os.listdir('.'):
        if filename.endswith('.wav'):
            convert_wav_to_header(filename)

if __name__ == '__main__':
    main()