# News Summarization and Text-to-Speech Application

## Overview
This project is a web-based application that extracts key details from multiple news articles related to a specified company, performs sentiment analysis, conducts comparative analysis, and generates text-to-speech (TTS) output in Hindi. Users can input a company name and receive a structured sentiment report along with an audio output.

## Project Structure
```
news-summarization-tts
├── app.py                # Main entry point of the application
├── api.py                # API endpoints for news extraction and analysis
├── utils.py              # Utility functions for scraping and analysis
├── requirements.txt      # Project dependencies
├── README.md             # Documentation for the project
├── templates
│   └── index.html        # HTML template for the web interface
├── static
│   ├── css
│   │   └── style.css     # CSS styles for the web interface
│   └── js
│       └── script.js     # JavaScript for client-side interactions
└── tests
    └── test_app.py       # Unit tests for the application
```

## Setup Instructions
1. **Clone the Repository**
   ```
   git clone <repository-url>
   cd news-summarization-tts
   ```

2. **Install Dependencies**
   Use the following command to install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Application**
   Start the application by running:
   ```
   python app.py
   ```
   The application will be accessible at `http://localhost:8501`.

## Usage
- Input a company name in the provided text box.
- Click the submit button to fetch news articles and generate the sentiment report.
- The application will display the titles, summaries, sentiments, and key topics of the articles.
- An audio file summarizing the sentiment report will be available for playback.

## Models Used
- **News Extraction**: Utilizes BeautifulSoup for web scraping to gather news articles.
- **Sentiment Analysis**: Implements a sentiment analysis model to classify articles as Positive, Negative, or Neutral.
- **Text-to-Speech (TTS)**: Uses an open-source TTS model to convert the summarized content into Hindi speech.

## API Development
The application exposes several API endpoints for:
- Fetching news articles based on the company name.
- Performing sentiment analysis on the articles.
- Generating TTS audio from the summarized content.

## Assumptions & Limitations
- The application assumes that the input company name will yield relevant news articles.
- The scraping functionality may be limited by the structure of the target websites.
- TTS output quality may vary based on the model used.

## Contribution
Feel free to contribute to this project by submitting issues or pull requests. Your feedback and suggestions are welcome!