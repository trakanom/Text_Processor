# Text Processor

Text Processor is a simple Python-based web application that processes text input to remove stopwords, lemmatize words, and generate optional word cloud and histogram visualizations.

## Features

- Remove stopwords
- Lemmatize words
- Generate word cloud (optional)
- Generate histogram (optional)

## Installation

To set up the environment and install the required packages, run the following command:

```bash
pip install nltk flask matplotlib
```

## Usage

1. Run the `app.py` file:

   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000`.

3. Paste your text in the input field, choose the desired options (word cloud, histogram), and click "Process Text".

4. The processed text will be displayed along with any generated visualizations.

## Dependencies

- NLTK
- Flask
- Matplotlib

## License

MIT License
