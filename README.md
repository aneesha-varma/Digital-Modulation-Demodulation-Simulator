# 📡 Digital Modulation and Demodulation Simulator

## 📌 Project Overview

The **Digital Modulation and Demodulation Simulator** is a Python-based interactive application developed for the Principles of Communication subject.

This project demonstrates digital communication using three modulation techniques:

- ASK – Amplitude Shift Keying
- FSK – Frequency Shift Keying
- BPSK – Binary Phase Shift Keying

The application converts text messages into binary data, generates modulated signals, simulates noise during transmission, and recovers the original message through demodulation.

## 🎯 Objectives

- Understand the fundamentals of digital communication.
- Implement ASK, FSK, and BPSK modulation techniques.
- Convert text messages into binary data.
- Simulate signal transmission through a noisy channel.
- Recover transmitted information using demodulation.
- Calculate Bit Error Rate (BER).
- Visualize transmitted and received signal waveforms.

## ✨ Features

- Text-to-binary conversion.
- ASK, FSK, and BPSK modulation.
- AWGN (Additive White Gaussian Noise) simulation.
- Adjustable Signal-to-Noise Ratio (SNR).
- Digital signal waveform visualization.
- Demodulation and message recovery.
- Bit Error Rate calculation.
- Original and received data comparison.
- Interactive Streamlit interface.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web application interface |
| NumPy | Numerical and signal calculations |
| Matplotlib | Signal waveform visualization |
| VS Code | Development environment |
| Git | Version control |
| GitHub | Project hosting |

## 📂 Project Structure

```text
Digital-Modulation-Demodulation-Simulator/
│
├── app.py
│
├── modules/
│   ├── __init__.py
│   ├── encoding.py
│   ├── modulation.py
│   ├── channel.py
│   └── demodulation.py
│
├── screenshots/
│   ├── Screenshot 2026-11-05 203129.png
│   ├── Screenshot 2026-11-05 203303.png
│   ├── Screenshot 2026-11-05 203358.png
│   ├── Screenshot 2026-11-05 203434.png
│   └── Screenshot 2026-11-05 203513.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 📸 Project Screenshots

The following screenshots demonstrate the application interface and its simulation results.

### Screenshot 1 – Application Interface

![Application Interface](screenshots/Screenshot%202026-11-05%20203129.png)

### Screenshot 2 – Simulation Interface

![Simulation Interface](screenshots/Screenshot%202026-11-05%20203303.png)

### Screenshot 3 – Modulation Results

![Modulation Results](screenshots/Screenshot%202026-11-05%20203358.png)

### Screenshot 4 – Signal Waveform Visualization

![Signal Waveform Visualization](screenshots/Screenshot%202026-11-05%20203434.png)

### Screenshot 5 – Demodulation and Analysis

![Demodulation and Analysis](screenshots/Screenshot%202026-11-05%20203513.png)

## ⚙️ Working Methodology

The project follows these steps:

1. **Input:** The user enters a text message.
2. **Encoding:** The text message is converted into binary bits.
3. **Modulation:** Binary data is converted into ASK, FSK, or BPSK signals.
4. **Channel Simulation:** AWGN noise is added to the transmitted signal.
5. **Demodulation:** The receiver extracts binary information from the received signal.
6. **Decoding:** The recovered binary data is converted back into text.
7. **Performance Analysis:** BER and SNR are calculated and displayed.

## 📡 Digital Modulation Techniques

### 1. ASK – Amplitude Shift Keying

ASK represents binary data by changing the amplitude of the carrier signal.

### 2. FSK – Frequency Shift Keying

FSK represents binary data using different carrier frequencies.

### 3. BPSK – Binary Phase Shift Keying

BPSK represents binary data using two carrier phases separated by 180 degrees.

## 📊 Performance Parameters

**Signal-to-Noise Ratio (SNR):**

Measures the signal power relative to the noise power.

**Bit Error Rate (BER):**

Measures the proportion of incorrectly received bits.

\[
BER = \frac{\text{Number of Bit Errors}}{\text{Total Transmitted Bits}}
\]

A higher SNR generally results in fewer transmission errors.

## 💻 Installation and Execution

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Digital-Modulation-Demodulation-Simulator.git
```

### Step 2: Navigate to the project directory

```bash
cd Digital-Modulation-Demodulation-Simulator
```

### Step 3: Create a virtual environment

```bash
python -m venv venv
```

### Step 4: Activate the virtual environment

For Windows PowerShell:

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

The application will open in your browser at:

```text
http://localhost:8501
```

## 🧪 Testing

The application can be tested using different messages and modulation techniques.

| Test | Message | Technique | SNR |
|---|---|---|---|
| 1 | HELLO | ASK | 30 dB |
| 2 | DIGITAL | FSK | 30 dB |
| 3 | SIGNAL | BPSK | 30 dB |
| 4 | HELLO WORLD | ASK | 5 dB |
| 5 | COMMUNICATION | FSK | 10 dB |

## 🌍 Applications

- Digital communication systems.
- Wireless communication.
- Radio communication.
- Signal processing education.
- Communication system simulation.

## 🚀 Future Enhancements

- Implement QPSK and QAM modulation.
- Add BER versus SNR comparison graphs.
- Implement advanced noise filtering.
- Add real-time signal transmission.
- Add downloadable simulation reports.
- Compare the performance of different modulation techniques.

## 📝 Conclusion

The Digital Modulation and Demodulation Simulator provides an interactive demonstration of digital communication principles. It helps users understand modulation, demodulation, signal transmission, noise effects, and data recovery through practical simulation.

---

**Developed as a Principles of Communication Mini Project.**