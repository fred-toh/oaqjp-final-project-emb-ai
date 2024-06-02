# Import the libraries and packages
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector as detect

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    # Param from index.html
    text_to_analyze = request.args.get('textToAnalyze')
    resp = detect(text_to_analyze)

    return f"For the given statement, the system response is " \
            + f"'anger': {resp['anger']}, " \
            + f"'disgust': {resp['disgust']}, " \
            + f"'fear': {resp['fear']}, " \
            + f"'joy': {resp['joy']}, and " \
            + f"'sadness': {resp['sadness']}. " \
            + f"The dominant emotion is {resp['dominant_emotion']}."

@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.errorhandler(500)
def invalid_input():
    return ({"message": "Invalid input! Please try again."}, 500)

app.run(host = "0.0.0.0", port = "5000")