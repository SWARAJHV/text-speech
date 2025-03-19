from flask import Flask, request, jsonify, render_template
from utils import extract_news, perform_sentiment_analysis, generate_tts
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/news', methods=['POST'])
def get_news():
    company_name = request.json.get('company_name')
    articles = extract_news(company_name)
    return jsonify(articles)

@app.route('/api/sentiment', methods=['POST'])
def analyze_sentiment():
    articles = request.json.get('articles')
    sentiment_report = perform_sentiment_analysis(articles)
    return jsonify(sentiment_report)

@app.route('/api/tts', methods=['POST'])
def text_to_speech():
    summary = request.json.get('summary')
    audio_file = generate_tts(summary)
    return jsonify({"audio_file": audio_file})

if __name__ == '__main__':
    app.run(debug=True)