import numpy as np


def demodulate(signal, technique, samples_per_bit=1000):

    fs = 1000
    fc = 10

    t = np.arange(samples_per_bit) / fs

    recovered_bits = []

    for i in range(0, len(signal), samples_per_bit):

        segment = signal[i:i + samples_per_bit]

        if len(segment) != samples_per_bit:
            break

        if technique == "ASK":

            reference = np.cos(2 * np.pi * fc * t)

            amplitude = 2 * np.mean(segment * reference)

            bit = 1 if amplitude > 0.625 else 0

        elif technique == "FSK":

            reference_5 = np.cos(2 * np.pi * 5 * t)

            reference_10 = np.cos(2 * np.pi * 10 * t)

            score_5 = np.mean(segment * reference_5)

            score_10 = np.mean(segment * reference_10)

            bit = 1 if score_10 > score_5 else 0

        elif technique == "BPSK":

            reference = np.cos(2 * np.pi * fc * t)

            correlation = np.mean(segment * reference)

            bit = 1 if correlation >= 0 else 0

        else:
            raise ValueError("Invalid modulation technique")

        recovered_bits.append(bit)

    return recovered_bits