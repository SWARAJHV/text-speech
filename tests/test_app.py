import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Company Name' in response.data

def test_sentiment_analysis(client):
    response = client.post('/analyze', data={'company_name': 'Tesla'})
    assert response.status_code == 200
    assert b'Tesla' in response.data
    assert b'Positive' in response.data or b'Negative' in response.data or b'Neutral' in response.data

def test_news_extraction(client):
    response = client.post('/extract', data={'company_name': 'Tesla'})
    assert response.status_code == 200
    assert b'Title' in response.data
    assert b'Summary' in response.data

def test_tts_generation(client):
    response = client.post('/tts', data={'summary': 'Tesla’s latest news coverage is mostly positive.'})
    assert response.status_code == 200
    assert b'Audio' in response.data

def test_invalid_company_name(client):
    response = client.post('/analyze', data={'company_name': ''})
    assert response.status_code == 400
    assert b'Invalid company name' in response.data