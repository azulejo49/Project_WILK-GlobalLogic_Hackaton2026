//architecture.md

# Project WILK - System Architecture

Our architecture is designed for **ultra-low power consumption** and **infinite scalability** in harsh physical environments.

## 1. The Edge Node (Hardware & AI)
* **Hardware:** Microcontroller with an integrated MEMS microphone (e.g., ESP32 or Arduino Nano 33 BLE Sense). Powered by a 5V mini solar panel and Li-Ion battery.
* **Edge Computing:** Raw audio is NEVER sent to the cloud. A TinyML model (compiled via Edge Impulse) runs locally in C++. It extracts the Mel-frequency cepstral coefficients (MFCCs) of the sound and classifies it as `Normal` or `Anomaly`.

## 2. The Cloud Gateway
* **Protocol:** MQTT / HTTP. When the edge model detects an anomaly with >85% confidence, it wakes its radio and transmits a 50-byte JSON payload: `{"node_id": "WILK_01", "status": "anomaly", "confidence": 0.94}`.
* **Backend:** A Python web server processes incoming telemetry and maintains the global state of the infrastructure.

## 3. The Digital Twin Dashboard
* **Frontend:** A lightweight HTML/JS web interface polls the cloud gateway. Upon receiving a state change, it alerts operators in real-time, providing the exact node location and timestamp of the acoustic degradation.