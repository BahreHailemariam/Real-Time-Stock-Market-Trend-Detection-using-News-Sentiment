# 🧠 Real-Time Stock Market Trend Detection using News Sentiment

## 📘 Project Overview
This project leverages **Natural Language Processing (NLP)** and **real-time news sentiment analysis** to detect and predict stock market trends.  
By analyzing live financial news streams, social media posts, and headlines, the system identifies **positive or negative market sentiment** and correlates it with stock price movements to forecast short-term trends.

The pipeline integrates **text analytics, sentiment modeling, and visualization dashboards** for data-driven investment insights.

---

## 🚀 Key Objectives
- Analyze live financial news and stock market data in real-time.
- Determine **sentiment polarity** (positive, neutral, negative) using NLP.
- Correlate sentiment scores with market indicators like price, volume, and volatility.
- Visualize insights through **Power BI** and **Streamlit** dashboards.
- Enable real-time alerts for trend shifts or market sentiment changes.

---

## 🧩 Workflow Summary

### 1. **Data Ingestion**
- Collect live financial news headlines and articles using APIs (e.g., NewsAPI, Finviz, or Reddit Finance threads).
- Fetch stock prices and technical indicators using `yfinance` or Alpha Vantage API.

### 2. **Preprocessing**
- Clean raw text (remove URLs, HTML tags, stopwords, punctuation).
- Tokenize and normalize text using **NLTK** or **spaCy**.
- Map each article to its corresponding stock ticker.

### 3. **Sentiment Analysis**
- Apply pretrained NLP models like **VADER**, **TextBlob**, or **FinBERT** to compute sentiment polarity.
- Assign sentiment scores:  
  - Positive → 1  
  - Neutral → 0  
  - Negative → -1

### 4. **Feature Engineering**
- Aggregate sentiment scores per company or time window (e.g., hourly, daily).
- Merge with market metrics: price change %, volume, and volatility index (VIX).

### 5. **Model Training**
- Train **LSTM**, **Random Forest**, or **Gradient Boosting** models to predict short-term stock trends.
- Evaluate performance using **AUC, RMSE, Precision, Recall**.

### 6. **Visualization & Deployment**
- Real-time dashboards built with:
  - **Power BI:** Trend visualization, sentiment heatmaps, and KPIs.
  - **Streamlit:** Interactive prediction app for live sentiment analysis.

---
