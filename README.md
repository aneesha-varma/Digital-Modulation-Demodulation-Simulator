# Digital Modulation and Demodulation Simulator

## Project Overview

The Digital Modulation and Demodulation Simulator is a Python-based application developed for the Principles of Communication subject.

The project demonstrates how digital information is transmitted through a communication channel using different digital modulation techniques.

It implements ASK (Amplitude Shift Keying), FSK (Frequency Shift Keying), and BPSK (Binary Phase Shift Keying).

The application converts text messages into binary data, generates modulated signals, adds noise to simulate a real communication channel, and performs demodulation to recover the original message.

## Objectives

- To understand the fundamentals of digital communication.
- To implement ASK, FSK, and BPSK modulation techniques.
- To convert text messages into binary data.
- To simulate signal transmission through a noisy channel.
- To recover transmitted information using demodulation.
- To calculate Bit Error Rate (BER).
- To visualize transmitted and received signals.

## Features

- Text-to-binary conversion.
- ASK, FSK, and BPSK modulation.
- AWGN (Additive White Gaussian Noise) channel simulation.
- Adjustable Signal-to-Noise Ratio (SNR).
- Digital signal waveform visualization.
- Demodulation and message recovery.
- Bit Error Rate calculation.
- Comparison of original and received messages.

## Technologies Used

- Python
- Streamlit
- NumPy
- Matplotlib
- Visual Studio Code
- Git and GitHub

## Project Structure

```text
Digital-Modulation-Demodulation-Simulator/
│
├── app.py
├── modules/
│   ├── __init__.py
│   ├── encoding.py
│   ├── modulation.py
│   ├── channel.py
│   └── demodulation.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Working Methodology

1. Input: The user enters a text message.
2. Encoding: The text message is converted into binary bits.
3. Modulation: Binary data is converted into ASK, FSK, or BPSK signals.
4. Channel: AWGN noise is added to the modulated signal.
5. Demodulation: The receiver extracts the binary information from the noisy signal.
6. Decoding: The recovered binary data is converted back into text.
7. Analysis: The application calculates BER and displays signal waveforms.

## Digital Modulation Techniques

### 1. ASK – Amplitude Shift Keying

In ASK, the amplitude of the carrier signal changes according to the input binary data.

### 2. FSK – Frequency Shift Keying

In FSK, different carrier frequencies represent binary 0 and binary 1.

### 3. BPSK – Binary Phase Shift Keying

In BPSK, the phase of the carrier signal changes by 180 degrees to represent binary information.

## Installation and Execution

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Digital-Modulation-Demodulation-Simulator.git
```

### Step 2: Navigate to the project

```bash
cd Digital-Modulation-Demodulation-Simulator
```

### Step 3: Create a virtual environment

```bash
python -m venv venv
```

### Step 4: Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the application

```bash
streamlit run app.py
```

The application will open in your web browser.

## Results

The application displays:

- Original binary data.
- Modulated signal waveform.
- Received signal with noise.
- Demodulated binary data.
- Recovered text message.
- Bit Error Rate (BER).
- Signal-to-Noise Ratio (SNR).

## Applications

- Digital communication systems.
- Wireless communication.
- Radio communication.
- Signal processing education.
- Communication system simulation.

## Future Enhancements

- Add QPSK and QAM modulation.
- Implement advanced noise filtering.
- Add real-time signal transmission.
- Compare the performance of different modulation techniques.
- Add graphical BER versus SNR analysis.

## Conclusion

The Digital Modulation and Demodulation Simulator demonstrates the basic working principles of digital communication systems. It provides a visual and interactive way to understand modulation, demodulation, noise effects, and successful data transmission.

---

**Developed as a Principles of Communication Mini Project.**