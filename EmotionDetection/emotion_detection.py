from flask import Flask
import requests, json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = myobj, headers=header)
    formatted_response = response.json()
    scores = formatted_response['emotionPredictions'][0]['emotion']
    anger = scores['anger']
    disgust = scores['disgust']
    fear = scores['fear']
    joy = scores['joy']
    sadness = scores['sadness']
    dominant_emotion = max(scores, key=scores.get)
    formatted_emotions = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
    return formatted_emotions
