//edge_node/simulate_anomaly.py

import requests
import time
import random

CLOUD_URL = "http://localhost:5000/alert"

def simulate_edge_detection():
    print("🎙️ WILK_01 Edge Node Initialized.")
    print("👂 Listening for acoustic anomalies...")
    
    # Fake processing delay for dramatic effect during the demo
    time.sleep(2) 
    
    # Generate a fake high confidence score from our "AI"
    confidence_score = round(random.uniform(92.0, 99.9), 2)
    
    print(f"⚠️ HIGH FREQUENCY GRINDING DETECTED! Confidence: {confidence_score}%")
    print("📡 Waking radio and transmitting alert to cloud...")
    
    payload = {
        "node_id": "WILK_01",
        "status": "anomaly",
        "confidence": confidence_score
    }
    
    try:
        response = requests.post(CLOUD_URL, json=payload)
        if response.status_code == 200:
            print("✅ Alert successfully transmitted. Going back to sleep to save power.")
        else:
            print("❌ Failed to reach cloud gateway.")
    except Exception as e:
        print(f"❌ Connection error: {e}")

if __name__ == "__main__":
    simulate_edge_detection()