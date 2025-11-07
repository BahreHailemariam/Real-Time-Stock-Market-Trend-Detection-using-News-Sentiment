# Fetch financial news via API
"""
fetch_news.py
-------------
Fetches live or historical financial news using the NewsAPI.
Stores results in data/raw/news_headlines.csv
"""

import requests
import pandas as pd
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY", "demo_api_key")

def fetch_financial_news(query="stock market", page_size=50):
    """Fetch latest financial news headlines."""
    url = f"https://newsapi.org/v2/everything?q={query}&language=en&pageSize={page_size}&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("status") != "ok":
        raise Exception(f"API Error: {data.get('message')}")

    articles = data["articles"]
    df = pd.DataFrame([
        {
            "source": a["source"]["name"],
            "title": a["title"],
            "description": a["description"],
            "publishedAt": a["publishedAt"]
        } for a in articles
    ])
    df["fetched_at"] = datetime.utcnow()
    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/news_headlines.csv", index=False)
    print(f"✅ Saved {len(df)} news articles to data/raw/news_headlines.csv")

if __name__ == "__main__":
    fetch_financial_news("NASDAQ OR Dow Jones")
