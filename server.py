from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotions():
    textToAnalyze = request.args.get("textToAnalyze")
    response = emotion_detector(textToAnalyze)

    formatted_response = f"For the given statement, the system response is 'anger': {response["anger"]}, 'disgust': {response["disgust"]}, 'fear': {response["fear"]}, 'joy': {response["joy"]}, 'sadness': {response["sadness"]}. The dominant emotion is {response["dominant_emotion"]}"

    return formatted_response