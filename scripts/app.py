# Streamlit dashboard for real-time prediction
"""
app.py
------
Streamlit app for real-time sentiment-based stock trend prediction.
"""

import streamlit as st
import pandas as pd
import joblib
import datetime

model = joblib.load("models/sentiment_model.pkl")

st.set_page_config(page_title="📈 Real-Time Stock Sentiment Dashboard", layout="wide")
st.title("📈 Real-Time Stock Market Trend Detection using News Sentiment")

st.sidebar.header("Input Parameters")
avg_sentiment = st.sidebar.slider("Average Sentiment", -1.0, 1.0, 0.1)
sentiment_shift = st.sidebar.slider("Sentiment Shift", -1.0, 1.0, 0.0)
price_change = st.sidebar.slider("Price Change (%)", -0.1, 0.1, 0.0)

if st.sidebar.button("Predict Trend"):
    input_data = pd.DataFrame({
        "avg_sentiment": [avg_sentiment],
        "sentiment_shift": [sentiment_shift],
        "price_change": [price_change]
    })
    pred = model.predict(input_data)[0]
    label = "📈 Uptrend Expected" if pred == 1 else "📉 Downtrend Expected"
    st.success(label)

st.markdown("---")
st.markdown(f"📅 Last updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
