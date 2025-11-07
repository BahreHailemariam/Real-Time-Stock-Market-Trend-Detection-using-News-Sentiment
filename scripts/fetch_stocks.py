# Download stock market data
"""
fetch_stocks.py
---------------
Downloads recent stock market data using yfinance API.
Stores results in data/raw/stock_prices.csv
"""

import yfinance as yf
import pandas as pd
import os

def fetch_stock_data(tickers=["AAPL", "MSFT", "AMZN"], period="5d", interval="1h"):
    all_data = []
    for ticker in tickers:
        df = yf.download(ticker, period=period, interval=interval)
        df.reset_index(inplace=True)
        df["Ticker"] = ticker
        all_data.append(df)

    combined = pd.concat(all_data)
    os.makedirs("data/raw", exist_ok=True)
    combined.to_csv("data/raw/stock_prices.csv", index=False)
    print(f"✅ Saved stock prices for {len(tickers)} tickers")

if __name__ == "__main__":
    fetch_stock_data()
