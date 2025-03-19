import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from gtts import gTTS
import os

def scrape_news_articles(company_name, num_articles=10):
    search_url = f"https://news.google.com/search?q={company_name}&hl=en-US&gl=US&ceid=US:en"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = []
    for item in soup.find_all('article')[:num_articles]:
        title = item.find('h3').text
        summary = item.find('p').text if item.find('p') else ''
        link = item.find('a')['href']
        articles.append({
            'title': title,
            'summary': summary,
            'link': link
        })    
    return articles

def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

def generate_summary(text):
    # Placeholder for a more sophisticated summarization algorithm
    sentences = text.split('. ')
    return '. '.join(sentences[:2])  # Return the first two sentences as a summary

def text_to_speech(text, lang='hi'):
    tts = gTTS(text=text, lang=lang)
    audio_file = 'output.mp3'
    tts.save(audio_file)
    return audio_file

def clean_up_audio_file(audio_file):
    if os.path.exists(audio_file):
        os.remove(audio_file)