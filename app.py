import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from modules.encoding import text_to_binary, binary_to_text
from modules.modulation import modulate
from modules.channel import add_noise
from modules.demodulation import demodulate


# Page configuration
st.set_page_config(
    page_title="Digital Modulation Simulator",
    page_icon="📡",
    layout="wide"
)


# Application heading
st.title("📡 Digital Modulation and Demodulation Simulator")

st.markdown("""
This application demonstrates digital communication using
ASK, FSK and BPSK modulation techniques.

Enter a message, select a modulation technique and observe
how the signal is transmitted through a noisy channel.
""")

st.divider()


# User inputs
st.subheader("1. Enter Communication Details")

message = st.text_input(
    "Enter your text message:",
    value="HELLO"
)

col1, col2 = st.columns(2)

with col1:
    technique = st.selectbox(
        "Select Modulation Technique",
        ["ASK", "FSK", "BPSK"]
    )

with col2:
    snr_db = st.slider(
        "Select Signal-to-Noise Ratio (SNR) in dB",
        min_value=0,
        max_value=30,
        value=15
    )


# Start simulation
if st.button("🚀 Start Simulation", type="primary"):

    if not message.strip():

        st.warning("Please enter a valid message.")

    else:

        # Step 1: Text to binary
        bits = text_to_binary(message)

        # Step 2: Modulation
        time, modulated_signal, fs = modulate(
            bits,
            technique
        )

        # Step 3: Add channel noise
        received_signal = add_noise(
            modulated_signal,
            snr_db
        )

        # Step 4: Demodulation
        recovered_bits = demodulate(
            received_signal,
            technique
        )

        # Step 5: Binary to text
        recovered_message = binary_to_text(
            recovered_bits
        )

        # Step 6: Calculate BER
        errors = sum(
            original != recovered
            for original, recovered
            in zip(bits, recovered_bits)
        )

        ber = errors / len(bits) if bits else 0

        # Signal power and noise power
        noise = received_signal - modulated_signal

        signal_power = np.mean(modulated_signal ** 2)
        noise_power = np.mean(noise ** 2)

        actual_snr = (
            10 * np.log10(signal_power / noise_power)
            if noise_power > 0 else float("inf")
        )

        st.divider()

        # Results
        st.subheader("2. Simulation Results")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Modulation", technique)

        c2.metric("Total Bits", len(bits))

        c3.metric("Bit Errors", errors)

        c4.metric("BER", f"{ber:.4f}")

        st.write(f"**Selected SNR:** {snr_db} dB")
        st.write(f"**Measured SNR:** {actual_snr:.2f} dB")

        st.divider()

        # Binary data
        st.subheader("3. Binary Data")

        st.write("**Original Message:**", message)

        st.code(
            ''.join(map(str, bits)),
            language="text"
        )

        st.write("**Recovered Binary Data:**")

        st.code(
            ''.join(map(str, recovered_bits)),
            language="text"
        )

        st.divider()

        # Recovered message
        st.subheader("4. Recovered Message")

        if recovered_message == message:

            st.success(
                f"Successful Transmission! Message: {recovered_message}"
            )

        else:

            st.warning(
                f"Received Message: {recovered_message}"
            )

        # Error information
        if errors == 0:

            st.success("No bit errors detected.")

        else:

            st.error(
                f"{errors} bit error(s) detected during transmission."
            )

        st.divider()

        # Waveform visualization
        st.subheader("5. Signal Waveform Visualization")

        # Display first 12 bits to make graphs readable
        display_bits = min(12, len(bits))

        display_samples = display_bits * 1000

        display_time = time[:display_samples]

        display_original = modulated_signal[:display_samples]

        display_received = received_signal[:display_samples]

        fig, axes = plt.subplots(
            4, 1,
            figsize=(14, 12)
        )

        # Original binary data
        bit_time = np.arange(display_bits + 1)

        axes[0].step(
            bit_time[:-1],
            bits[:display_bits],
            where="post"
        )

        axes[0].set_title("Original Binary Data")
        axes[0].set_ylabel("Bit Value")
        axes[0].set_ylim(-0.3, 1.3)
        axes[0].set_xticks(bit_time)
        axes[0].grid(True)

        # Modulated signal
        axes[1].plot(
            display_time,
            display_original
        )

        axes[1].set_title(
            f"{technique} Modulated Signal"
        )

        axes[1].set_ylabel("Amplitude")
        axes[1].grid(True)

        # Noisy signal
        axes[2].plot(
            display_time,
            display_received
        )

        axes[2].set_title(
            "Received Signal with AWGN Noise"
        )

        axes[2].set_ylabel("Amplitude")
        axes[2].grid(True)

        # Recovered binary data
        axes[3].step(
            bit_time[:-1],
            recovered_bits[:display_bits],
            where="post"
        )

        axes[3].set_title("Demodulated Binary Data")
        axes[3].set_xlabel("Bit Interval")
        axes[3].set_ylabel("Bit Value")
        axes[3].set_ylim(-0.3, 1.3)
        axes[3].set_xticks(bit_time)
        axes[3].grid(True)

        plt.tight_layout()

        st.pyplot(fig)

        plt.close(fig)

        st.divider()

        # Comparison
        st.subheader("6. Transmission Analysis")

        st.write(
            f"Original Message: **{message}**"
        )

        st.write(
            f"Recovered Message: **{recovered_message}**"
        )

        st.write(
            f"Number of errors: **{errors}**"
        )

        st.write(
            f"Bit Error Rate: **{ber:.4f}**"
        )

        st.progress(
            float(1 - ber),
            text=f"Successful Bit Recovery: {(1 - ber) * 100:.2f}%"
        )


# Footer
st.divider()

st.markdown("""
<div style="text-align:center">
    <p>Digital Modulation and Demodulation Simulator</p>
    <p>Principles of Communication Mini Project</p>
    <p>Developed using Python, NumPy, Matplotlib and Streamlit</p>
</div>
""", unsafe_allow_html=True)