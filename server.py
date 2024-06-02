''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''

# Import the libraries and packages
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector as detect

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the HTML interface as `textToAnalyze, 
        which is used as an argument to the `emotion_detector()` function,
        alias is `detect`. The returned response is a json dict, which is provided
        to the HTML interface as a formatted text, displaying each emotion's score
        and also the dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze') # Param from index.html

    resp = detect(text_to_analyze)

    if resp['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is \
            'anger': {resp['anger']}, \
            'disgust': {resp['disgust']}, \
            'fear': {resp['fear']}, \
            'joy': {resp['joy']}, and \
            'sadness': {resp['sadness']}. \
            The dominant emotion is {resp['dominant_emotion']}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

@app.errorhandler(500)
def invalid_input():
    ''' This is to handle errors. 
    '''
    return ({"message": "Invalid input! Please try again."}, 500)

app.run(host = "0.0.0.0", port = "5000")
