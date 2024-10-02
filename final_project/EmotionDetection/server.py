from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    # Get the JSON data from the request
    data = request.get_json()

    if 'text' not in data:
        return jsonify({"error": "Text input is required."}), 400

    # Get the text to analyze
    text_to_analyze = data['text']

    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)

    # Extract values for response message
    anger_score = result.get('anger', 0) 
    disgust_score = result.get('disgust', 0)
    fear_score = result.get('fear', 0)
    joy_score = result.get('joy', 0)
    sadness_score = result.get('sadness', 0)
    dominant_emotion = result.get('dominant_emotion', 'unknown')

    # Format the response message
    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, 'disgust': {disgust_score}, "
        f"'fear': {fear_score}, 'joy': {joy_score}, "
        f"'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
    )

    return jsonify(result=result, response_message=response_message)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

