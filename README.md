# **5G Channel Propagation and Noise Impact Simulation**

## **Introduction**
This project simulates the behavior of 5G signals under various propagation and noise conditions using MATLAB's 5G Toolbox. It aims to provide insights into signal degradation, enabling better design and optimization of 5G communication systems.

### **Features**
- **Waveform Generation**: 5G NR waveform with 16QAM modulation and 15 kHz subcarrier spacing.
- **Channel Modeling**: Realistic urban macro-cell propagation using the TDL-C profile.
- **Noise Simulation**: Additive White Gaussian Noise (AWGN) to emulate real-world conditions.
- **Performance Metrics**: Signal-to-Noise Ratio (SNR) and Bit Error Rate (BER) analysis.
- **Visualizations**: Time-domain and frequency-domain analysis with detailed plots.

---

## **Project Structure**
- **`init.m`**: Main script to generate the 5G NR waveform, apply channel effects, and add noise.
- **`BER.m`**: Script to compute and display the Bit Error Rate (BER).
- **Report**: Contains detailed theory and findings written in LaTeX.
- **Visualizations**: Plots showcasing signal behavior under different conditions.

---

## **Key Methodologies**

### **Waveform Generation**
- Modulation: **16QAM**.
- Subcarrier Spacing: **15 kHz**.
- Resource Blocks: **100**.

### **Channel Modeling**
- Profile: **TDL-C** (Tapped Delay Line - Case C).
- Delay Spread: **300 ns**.
- Doppler Shift: **50 Hz**.

### **Noise Addition**
- Target SNR: **20 dB**.
- Noise modeled using AWGN, introducing realistic impairments.

### **Performance Metrics**
1. **Signal-to-Noise Ratio (SNR)**:
   $\text{SNR} = 10 \cdot \log_{10} \left( \frac{P_{\text{signal}}}{P_{\text{noise}}} \right)$
2. **Bit Error Rate (BER)**:
   $\text{BER} = \frac{\text{Number of Bit Errors}}{\text{Total Number of Bits}}$

---

## **Results**

### **1. Time Domain Analysis**
- **Original Waveform**: Clean signal without impairments.
- **After Channel Effects**: Shows multipath propagation-induced attenuation.
- **After Adding Noise**: Significant degradation due to AWGN.


---

### **2. Frequency Domain Analysis**
- **Original Spectrum**: Bandwidth is preserved.
- **After Channel Effects**: Minor distortions due to multipath.
- **After Noise Addition**: Significant noise-induced distortions.



---

### **3. SNR Analysis**
- Target SNR: **20 dB**.
- Measured SNR: **20.0041 dB**.


---

### **4. BER Analysis**
- Total Transmitted Bits: 2,000,000.
- Bit Errors: 1,006,500.
- **BER**: 0.50325 (uncoded system).

---

## **Technologies Used**
- MATLAB **5G Toolbox**:
  - `nrWavegen*` functions for waveform generation.
  - `nrTDLChannel` for channel modeling.
  - Standard-compliant 5G configurations.
- Visualization with MATLAB plotting functions.

---

## **Usage**
1. Clone this repository.
2. Open MATLAB and navigate to the project directory.
3. Run `init.m` to generate the waveform and apply noise.
4. Run `BER.m` to compute the Bit Error Rate.

---

## **Demonstration**
https://drive.google.com/file/d/1wA9psaybtLXcQZvOO2kd596hA8zPC86M/view?usp=sharing

---

## **Future Scope**
- **MIMO Configurations**: Incorporate beamforming and spatial diversity.
- **Higher-Order Modulations**: Explore 64QAM and 256QAM.
- **Error Correction**: Integrate coding techniques to mitigate BER.

---

## **Acknowledgment**
Special thanks to Dr. Bhupendra Kumar for his guidance and insights into 5G technology.

---

## **References**
1. MATLAB 5G Toolbox Documentation, MathWorks.  
2. A. F. Molisch, *Wireless Communications*. John Wiley & Sons, 2011.  
3. 3GPP TS 38.211 V15.4.0, "NR; Physical Channels and Modulation."  

---

