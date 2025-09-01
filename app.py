import os
import httpx
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
from datetime import datetime
import json

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask application.
app = Flask("voice_presentation_app")

# In-memory logging (in production, use a database)
presentation_logs = []

# Serve the HTML page at the root route.
@app.route("/")
def index():
    try:
        return render_template("index.html")
    except Exception as e:
        return "index.html not found", 404

# The /session endpoint
@app.route("/session", methods=["GET"])
def session_endpoint():
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    if not openai_api_key:
        return jsonify({"error": "OPENAI_API_KEY not set"}), 500

    # Make a synchronous POST request to the OpenAI realtime sessions endpoint
    with httpx.Client() as client:
        r = client.post(
            "https://api.openai.com/v1/realtime/sessions",
            headers={
                "Authorization": f"Bearer {openai_api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-4o-mini-realtime-preview",
                "voice": "alloy",
            },
        )
        #"gpt-4o-realtime-preview-2024-12-17"
        data = r.json()
        print(data)
        return jsonify(data)

# Logging endpoint
@app.route("/logs")
def logs():
    return render_template("logs.html", logs=presentation_logs)

# API endpoint to log events
@app.route("/api/log", methods=["POST"])
def log_event():
    try:
        log_data = request.get_json()
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "event": log_data.get("event"),
            "data": log_data.get("data", {}),
            "slide": log_data.get("slide", 1)
        }
        presentation_logs.append(log_entry)
        return jsonify({"status": "logged"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to get current slide
@app.route("/api/slide/<int:slide_number>", methods=["POST"])
def update_slide(slide_number):
    try:
        # Log slide change
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "event": "slide_change",
            "data": {"new_slide": slide_number},
            "slide": slide_number
        }
        presentation_logs.append(log_entry)
        return jsonify({"status": "slide_updated", "slide": slide_number})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Run the Flask app on port 8116
    app.run(host="0.0.0.0", port=8116, debug=True)
