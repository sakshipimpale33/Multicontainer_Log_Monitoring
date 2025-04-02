from flask import Flask, jsonify
import logging
import requests
import threading
import time
import signal
import sys
import random  # Import random for simulating anomalies

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

stop_event = threading.Event()  # Event to control the loop

@app.route("/api", methods=["GET"])
def get_data():
    app.logger.info("Flask API called")

    # Simulate anomalies
    random_value = random.random()
    if random_value < 0.1:
        # 10% chance of returning a 500 error
        app.logger.error("Simulated server error")
        return jsonify({"error": "Internal Server Error"}), 500
    elif random_value < 0.2:
        # 10% chance of introducing a delay
        app.logger.warning("Simulated delay in response")
        time.sleep(3)  # 3-second delay
        return jsonify({"message": "Delayed response from Flask API!"})
    else:
        # Normal response
        return jsonify({"message": "Hello from Flask API!"})

# Function to continuously hit the API with a delay
def hit_api_continuously():
    while not stop_event.is_set():
        try:
            response = requests.get("http://localhost:5000/api")
            app.logger.info(f"API Response: {response.json()}")
        except Exception as e:
            app.logger.error(f"Error hitting API: {e}")
        time.sleep(2)  # 2-second delay

# Handle process termination
def handle_exit(signal, frame):
    app.logger.info("Stopping continuous API requests...")
    stop_event.set()  # Signal the thread to stop
    func = request.environ.get('werkzeug.server.shutdown')
    if func:
        func()  # Shut down the Flask server
    sys.exit(0)

if __name__ == "__main__":
    # Start the continuous API calls in a separate thread
    threading.Thread(target=hit_api_continuously, daemon=True).start()
    signal.signal(signal.SIGINT, handle_exit)  # Handle Ctrl+C
    signal.signal(signal.SIGTERM, handle_exit)  # Handle Docker stop
    app.run(host="0.0.0.0", port=5000)
