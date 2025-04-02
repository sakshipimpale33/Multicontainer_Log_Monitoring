from flask import Flask, jsonify
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route("/api", methods=["GET"])
def get_data():
    app.logger.info("Flask API called")
    return jsonify({"message": "Hello from Flask API!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
