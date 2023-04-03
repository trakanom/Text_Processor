import os
import string
from collections import Counter

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from flask import Flask, render_template, request

# from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.io as pio


nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("punkt")

app = Flask(__name__)


def process_text(text):
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Tokenize the text
    words = nltk.word_tokenize(text)

    # Remove stopwords and lemmatize the words
    lemmatizer = WordNetLemmatizer()
    processed_words = [
        lemmatizer.lemmatize(word.lower())
        for word in words
        if word.lower() not in stopwords.words("english")
    ]

    return processed_words


# def generate_wordcloud(words):
#     wc = WordCloud(width=800, height=400, max_words=100).generate(" ".join(words))
#     plt.imshow(wc, interpolation="bilinear")
#     plt.axis("off")
#     plt.savefig("static/wordcloud.png")


def generate_histogram(word_counts):
    labels, values = zip(*word_counts.items())

    trace = go.Bar(x=labels, y=values)
    data = [trace]
    layout = go.Layout(title="Word Frequency Histogram")
    fig = go.Figure(data=data, layout=layout)

    # Save the histogram to a file
    pio.write_image(fig, "static/histogram.png", format="png")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        # generate_wc = "wordcloud" in request.form
        generate_hist = "histogram" in request.form

        processed_words = process_text(text)

        # if generate_wc:
        #     generate_wordcloud(processed_words)

        if generate_hist:
            generate_histogram(processed_words)

        return render_template(
            "index.html",
            text=" ".join(processed_words),
            # wc=generate_wc,
            hist=generate_hist,
        )

    return render_template("index.html")


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
