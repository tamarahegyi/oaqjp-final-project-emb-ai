import requests
import json  # Import the json library to handle JSON serialization
from pprint import pprint

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyze}}
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json=myobj, headers=headers)

    # Convert the response text into a dictionary
    response_data = response.json()

    # Print the full response for debugging
    print("Response Data:", response_data)

    # Access the emotions from the first prediction
    emotions = response_data.get('emotionPredictions', [{}])[0].get('emotion', {})

    # Safely extract emotion scores
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)

    # Find the dominant emotion
    dominant_emotion = max(
        [('anger', anger_score), ('disgust', disgust_score), 
         ('fear', fear_score), ('joy', joy_score), 
         ('sadness', sadness_score)],
        key=lambda x: x[1]
    )[0]  # Get the name of the dominant emotion

    # Create the result dictionary
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

    # Return the result as a JSON string
    return result  # Serialize the dictionary to JSON format

if __name__ == "__main__":
    text = "I love the dark"  # Change the input text for testing
    result = emotion_detector(text)
    print(result)  # Print the result to see the output