#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install Python3 and try again."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null
then
    echo "pip3 is not installed. Please install pip3 and try again."
    exit 1
fi

# Install required packages
echo "Installing required packages..."
pip3 install -r requirements.txt

# Download NLTK data
echo "Downloading NLTK data..."
python3 -m nltk.downloader stopwords
python3 -m nltk.downloader wordnet

# Run the application
echo "Starting the Text Processor application..."
python3 app.py
