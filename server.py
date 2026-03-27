"""
server.py
Flask server for AI Emotion Detection App.
Includes error handling for blank input and PyLint-compliant docstrings.
"""

from flask import Flask, request, jsonify

# Import the emotion_detector function
try:
    from emotion_detection import emotion_detector
except ModuleNotFoundError:
    import sys
    sys.path.insert(0, './EmotionDetection')  # fallback if module is in a subfolder
    from emotion_detection import emotion_detector

# Initialize Flask app
app = Flask(__name__)


@app.route('/emotionDetector')
def detect_emotion():
    """
    Detect emotion from user input text.

    Query Parameter:
        textToAnalyze (str): Text to analyze for emotions.

    Returns:
        JSON response with emotion detection results if valid input,
        or error message with status 400 for blank input.
    """
    text = request.args.get('textToAnalyze', '')
    result = emotion_detector(text)

    if result["status_code"] == 400 or result["dominant_emotion"] is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    return jsonify(result)


@app.route('/')
def home():
    """
    Home route returning a simple message.
    """
    return "AI Emotion Detection App is running!", 200


if __name__ == '__main__':
    # Run the Flask server
    app.run(debug=False)
