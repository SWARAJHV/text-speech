from flask import Flask, request, jsonify
from utils import extract_news, perform_sentiment_analysis, generate_tts

app = Flask(__name__)

@app.route('/api/news', methods=['POST'])
def get_news():
    data = request.json
    company_name = data.get('company_name')
    articles = extract_news(company_name)
    return jsonify(articles)

@app.route('/api/sentiment', methods=['POST'])
def get_sentiment():
    data = request.json
    articles = data.get('articles')
    sentiment_results = perform_sentiment_analysis(articles)
    return jsonify(sentiment_results)

@app.route('/api/tts', methods=['POST'])
def get_tts():
    data = request.json
    summary = data.get('summary')
    audio_file = generate_tts(summary)
    return jsonify({'audio_file': audio_file})

if __name__ == '__main__':
    app.run(debug=True)