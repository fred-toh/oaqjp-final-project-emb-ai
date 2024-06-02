import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1'\
            +'/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id"\
                : "emotion_aggregated-workflow_lang_en_stock"}
    json_obj = { "raw_document": { "text": text_to_analyze } }

    emotions = {'anger': None, 'disgust': None, 'fear': None, \
                'joy': None, 'sadness': None, 'dominant_emotion': None}
    
    response = requests.post(url, json = json_obj, headers = header)

    status_code = response.status_code

    # print(status)

    if status_code == 400:
        return emotions
    else:
        json_dict = json.loads(response.text)
        emotions = json_dict['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key = lambda k: emotions[k])
        emotions['dominant_emotion'] = dominant_emotion
        return emotions