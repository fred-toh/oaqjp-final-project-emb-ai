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
    try:
        response = requests.post(url, json = json_obj, headers = header)
        json_dict = json.loads(response.text)
        emotions = json_dict['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions.items(), key = lambda x: x[1])
        emotions['dominant_emotion'] = dominant_emotion[0]
        return emotions

    except requests.exceptions.HTTPError as e:
        print(e.response.status_code) #status_code = 400
        # print(e.response.text)
        return emotions

    except Exception:
        return emotions

