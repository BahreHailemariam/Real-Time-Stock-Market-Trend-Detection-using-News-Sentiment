# Clean and preprocess news text
"""
preprocess_text.py
------------------
Cleans and tokenizes text data for sentiment analysis.
"""

import pandas as pd
import re
import spacy
from nltk.corpus import stopwords

nlp = spacy.load("en_core_web_sm")
STOPWORDS = set(stopwords.words("english"))

def clean_text(text):
    """Remove URLs, punctuation, numbers, and extra spaces."""
    text = re.sub(r"http\S+|www\S+|https\S+", "", str(text))
    text = re.sub(r"[^A-Za-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text.lower()

def preprocess_news(file_path="data/raw/news_headlines.csv"):
    df = pd.read_csv(file_path)
    df["cleaned"] = df["title"].fillna("").apply(clean_text)
    df["tokens"] = df["cleaned"].apply(lambda x: " ".join([t.lemma_ for t in nlp(x) if t.text not in STOPWORDS]))
    df.to_csv("data/processed/cleaned_news.csv", index=False)
    print("✅ Cleaned text saved to data/processed/cleaned_news.csv")

if __name__ == "__main__":
    preprocess_news()
