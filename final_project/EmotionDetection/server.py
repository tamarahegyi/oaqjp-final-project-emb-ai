from flask import Flask, request, jsonify
from emotion_detection import emotion_detector  # Adjust import according to your structure

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    # Get the JSON data from the request
    data = request.get_json()

    # Ensure that 'text' is included in the request
    if 'text' not in data or not data['text'].strip():  # Check for blank or missing text
        return jsonify({
            "message": "Invalid text! Please try again!"
        }), 400

    # Get the text to analyze
    text_to_analyze = data['text']

    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)  # Assuming this returns a dictionary

    # Extract values for response message
    anger_score = result.get('anger', 0)
    disgust_score = result.get('disgust', 0)
    fear_score = result.get('fear', 0)
    joy_score = result.get('joy', 0)
    sadness_score = result.get('sadness', 0)
    dominant_emotion = result.get('dominant_emotion', None)  # Allow for None value

    # Format the response message
    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, 'disgust': {disgust_score}, "
        f"'fear': {fear_score}, 'joy': {joy_score}, "
        f"'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
    )

    # Return the structured JSON and the response message
    return jsonify(result=result, response_message=response_message)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)  # Run the application on localhost:5000


