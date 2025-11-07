# Perform sentiment analysis using VADER/TextBlob/FinBERT
"""
sentiment_analysis.py
---------------------
Applies sentiment scoring to news headlines using VADER.
Outputs sentiment polarity and confidence.
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os

def compute_sentiment(input_file="data/processed/cleaned_news.csv"):
    analyzer = SentimentIntensityAnalyzer()
    df = pd.read_csv(input_file)
    df["compound"] = df["cleaned"].apply(lambda x: analyzer.polarity_scores(x)["compound"])
    df["sentiment"] = df["compound"].apply(lambda c: "positive" if c > 0.05 else ("negative" if c < -0.05 else "neutral"))

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/sentiment_scored.csv", index=False)
    print("✅ Sentiment scores saved to data/processed/sentiment_scored.csv")

if __name__ == "__main__":
    compute_sentiment()
