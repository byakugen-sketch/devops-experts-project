import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Doron!"

@app.route("/health")
def health():
    # Liveness and readiness probes hit this endpoint
    # Return 200 OK when the app is healthy and ready
    # In a real app this might check DB connections, cache availability etc.
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=5000, debug=debug)
