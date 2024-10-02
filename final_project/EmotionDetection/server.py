"""
server.py

This module provides a Flask application for detecting emotions from text input.
It includes an endpoint to analyze text and return associated emotion scores.
"""

from flask import Flask, request, jsonify
from . import emotion_detector

app = Flask(__name__)

INVALID_TEXT_MESSAGE = "Invalid text! Please try again!"
HTTP_BAD_REQUEST = 400
HTTP_INTERNAL_ERROR = 500

def create_response(result: dict, response_message: str) -> jsonify:
    """Creates a JSON response with emotion data and a message."""
    return jsonify(result=result, response_message=response_message)

def is_text_valid(data: dict) -> bool:
    """Checks if the input text is valid (not blank)."""
    return 'text' in data and bool(data['text'].strip())

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route() -> jsonify:
    """Handles emotion detection for POST requests."""
    data = request.get_json()

    # Validate the text input
    if not is_text_valid(data):
        return create_response({
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }, INVALID_TEXT_MESSAGE), HTTP_BAD_REQUEST

    text_to_analyze = data['text']

    try:
        result = emotion_detector(text_to_analyze)  # Assuming this returns a dictionary
    except (ValueError, TypeError) as e:
        return jsonify({"message": f"Error processing the input: {str(e)}"}), HTTP_INTERNAL_ERROR
    except Exception as e:
        return jsonify({"message": "An unexpected error occurred."}), HTTP_INTERNAL_ERROR

    anger_score = result.get('anger', 0)
    disgust_score = result.get('disgust', 0)
    fear_score = result.get('fear', 0)
    joy_score = result.get('joy', 0)
    sadness_score = result.get('sadness', 0)
    dominant_emotion = result.get('dominant_emotion', None)

    if dominant_emotion is None:
        return create_response({
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }, INVALID_TEXT_MESSAGE), HTTP_BAD_REQUEST

    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, 'disgust': {disgust_score}, "
        f"'fear': {fear_score}, 'joy': {joy_score}, "
        f"'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
    )

    return create_response(result, response_message)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)  # Run the application on localhost:5000
