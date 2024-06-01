import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1'\
            +'/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id"\
                : "emotion_aggregated-workflow_lang_en_stock"}
    json_obj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = json_obj, headers = header)
    json_dict = json.loads(response.text)
    emotions = json_dict['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions.items(), key = lambda x: x[1])
    emotions['dominant_emotion'] = dominant_emotion[0]
    if response.status_code == 200:
        return emotions