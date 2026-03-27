"""
server.py
Flask server for emotion detection application.
Handles requests to /emotionDetector and returns emotion analysis results.
"""

from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def detect_emotion():
    """
    Route to detect emotion from user input.

    Query Parameter:
        textToAnalyze (str): Text input from user for emotion detection.

    Returns:
        JSON response with emotion analysis results or error message for blank input.
    """
    text = request.args.get('textToAnalyze', '')
    result = emotion_detector(text)

    if result["status_code"] == 400 or result["dominant_emotion"] is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    return jsonify(result)


if __name__ == '__main__':
    # Starts the Flask server

