//backend/app.py

from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app) # Allows the HTML frontend to talk to this backend

# Global state to hold our machine's health
system_state = {
    "status": "Healthy",
    "color": "#28a745", # Green
    "last_event": "System initialized normally.",
    "timestamp": datetime.now().strftime("%H:%M:%S")
}

@app.route('/status', methods=['GET'])
def get_status():
    """Frontend polls this endpoint to get the current health status."""
    return jsonify(system_state)

@app.route('/alert', methods=['POST'])
def trigger_alert():
    """The Edge Node posts to this endpoint when it hears an anomaly."""
    data = request.json
    
    # Update the global state
    system_state["status"] = "CRITICAL ANOMALY DETECTED"
    system_state["color"] = "#dc3545" # Red
    system_state["last_event"] = f"Acoustic anomaly detected by {data.get('node_id')} with {data.get('confidence')}% confidence."
    system_state["timestamp"] = datetime.now().strftime("%H:%M:%S")
    
    print(f"🚨 ALERT RECEIVED: {system_state['last_event']}")
    return jsonify({"message": "Alert registered successfully"}), 200

if __name__ == '__main__':
    # Run the server on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)