"""
7b_error_handling_server.py
Flask server for AI Emotion Detection App with blank input error handling.
"""

from flask import Flask, request, jsonify

# Import the updated emotion_detector function
try:
    from emotion_detection import emotion_detector
except ModuleNotFoundError:
    import sys
    sys.path.insert(0, './EmotionDetection')  # fallback if emotion_detection.py is inside a folder
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
    # Start Flask server
    app.run(debug=True)
