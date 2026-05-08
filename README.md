# Project WILK: a Multi-Modal Edge AI Sentinel 🐺

**Evolve Hack 2026 | Theme 3: Intelligence in Motion** 

Disclaimer: Contest Project Proposal

Project WILK is a decentralized swarm of solar-powered edge nodes that use TinyML (Edge AI) to "listen" to the acoustic signatures, vibration detection, solar power telemetry, camera verification, Drone Auto Dispatch of industrial machinery and civil infrastructure.
By processing sound locally on the edge, it detects micro-anomalies and predicts catastrophic failures before they happen, sending low-bandwidth alerts to a central dashboard.

## Prerequisites
* Python 3.8+
* A web browser

## How to Run the Prototype

**Step 1: Start the Cloud Server**
Open a terminal, navigate to the `backend` folder, install dependencies, and run the server.
\`\`\`bash
cd backend
pip install -r requirements.txt
python app.py
\`\`\`
*The server will start on `http://localhost:5000`.*

**Step 2: Open the Dashboard**
Simply double-click the `frontend/index.html` file to open it in your browser. (Or serve it via Live Server in VS Code). The dashboard will show a "Healthy" green status.

**Step 3: Trigger the Edge Anomaly (The Hackathon Demo)**
Open a second terminal, navigate to the `edge_node` folder, and run the simulation script.
\`\`\`bash
cd edge_node
python simulate_anomaly.py
\`\`\`
Watch the dashboard instantly flip to RED, logging the acoustic anomaly!
//////////////////
-Multi-Modal Edge AI-Sound_Vibration_image_DroneV3- WILKV3.html-Project_WILK__The_SentinelsV3.mp4-WilkV3InfoGraph.png
