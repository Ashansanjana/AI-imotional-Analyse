import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_single_watson_nlp-1.8_cxx3770"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json = myobj, headers=headers)
    return response.text
