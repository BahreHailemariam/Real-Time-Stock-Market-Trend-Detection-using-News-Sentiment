# Combine sentiment and stock features
"""
feature_engineering.py
----------------------
Merges sentiment and stock price data.
Creates numerical features for model training.
"""

import pandas as pd
import numpy as np
import os

def engineer_features(sentiment_file="data/processed/sentiment_scored.csv", stock_file="data/raw/stock_prices.csv"):
    sentiment = pd.read_csv(sentiment_file)
    stocks = pd.read_csv(stock_file)

    # Aggregate sentiment by date
    sentiment["publishedAt"] = pd.to_datetime(sentiment["publishedAt"]).dt.date
    sentiment_summary = sentiment.groupby("publishedAt")["compound"].mean().reset_index()
    sentiment_summary.rename(columns={"compound": "avg_sentiment"}, inplace=True)

    stocks["Date"] = pd.to_datetime(stocks["Datetime"]).dt.date if "Datetime" in stocks.columns else pd.to_datetime(stocks["Date"]).dt.date
    merged = stocks.merge(sentiment_summary, left_on="Date", right_on="publishedAt", how="left")

    # Create features
    merged["price_change"] = merged["Close"].pct_change()
    merged["sentiment_shift"] = merged["avg_sentiment"].diff()
    merged["trend_label"] = np.where(merged["price_change"] > 0, 1, 0)

    os.makedirs("data/features", exist_ok=True)
    merged.to_csv("data/features/trend_features.csv", index=False)
    print("✅ Features saved to data/features/trend_features.csv")

if __name__ == "__main__":
    engineer_features()
