import numpy as np


def modulate(bits, technique, samples_per_bit=1000):
    fs = 1000
    bit_duration = 1.0
    fc = 10

    t = np.arange(samples_per_bit) / fs

    signal = []

    for bit in bits:

        if technique == "ASK":

            amplitude = 1.0 if bit == 1 else 0.25

            wave = amplitude * np.cos(
                2 * np.pi * fc * t
            )

        elif technique == "FSK":

            frequency = 10 if bit == 1 else 5

            wave = np.cos(
                2 * np.pi * frequency * t
            )

        elif technique == "BPSK":

            phase = 0 if bit == 1 else np.pi

            wave = np.cos(
                2 * np.pi * fc * t + phase
            )

        else:
            raise ValueError("Invalid modulation technique")

        signal.extend(wave)

    signal = np.array(signal)

    time = np.arange(len(signal)) / fs

    return time, signal, fs