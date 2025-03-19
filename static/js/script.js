document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('company-form');
    const resultContainer = document.getElementById('result-container');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const companyName = document.getElementById('company-name').value;

        fetch(`/api/news?company=${encodeURIComponent(companyName)}`)
            .then(response => response.json())
            .then(data => {
                displayResults(data);
            })
            .catch(error => {
                console.error('Error fetching news:', error);
                resultContainer.innerHTML = '<p>Error fetching news. Please try again.</p>';
            });
    });

    function displayResults(data) {
        resultContainer.innerHTML = '';

        const title = document.createElement('h2');
        title.textContent = `Sentiment Analysis for ${data.Company}`;
        resultContainer.appendChild(title);

        data.Articles.forEach(article => {
            const articleDiv = document.createElement('div');
            articleDiv.classList.add('article');

            const articleTitle = document.createElement('h3');
            articleTitle.textContent = article.Title;
            articleDiv.appendChild(articleTitle);

            const articleSummary = document.createElement('p');
            articleSummary.textContent = article.Summary;
            articleDiv.appendChild(articleSummary);

            const articleSentiment = document.createElement('p');
            articleSentiment.textContent = `Sentiment: ${article.Sentiment}`;
            articleDiv.appendChild(articleSentiment);

            const articleTopics = document.createElement('p');
            articleTopics.textContent = `Topics: ${article.Topics.join(', ')}`;
            articleDiv.appendChild(articleTopics);

            resultContainer.appendChild(articleDiv);
        });

        const comparativeAnalysis = document.createElement('h3');
        comparativeAnalysis.textContent = 'Comparative Sentiment Analysis';
        resultContainer.appendChild(comparativeAnalysis);

        const comparativeData = document.createElement('pre');
        comparativeData.textContent = JSON.stringify(data['Comparative Sentiment Score'], null, 2);
        resultContainer.appendChild(comparativeData);

        const finalSentiment = document.createElement('h3');
        finalSentiment.textContent = `Final Sentiment Analysis: ${data['Final Sentiment Analysis']}`;
        resultContainer.appendChild(finalSentiment);

        const audioLink = document.createElement('audio');
        audioLink.controls = true;
        audioLink.src = data.Audio;
        resultContainer.appendChild(audioLink);
    }
});