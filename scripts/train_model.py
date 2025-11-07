# Train ML models to predict market trends
"""
train_model.py
---------------
Trains predictive models to detect market trends from sentiment and price features.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
import joblib
import os

def train_model(feature_file="data/features/trend_features.csv"):
    df = pd.read_csv(feature_file).dropna(subset=["price_change", "avg_sentiment"])
    X = df[["avg_sentiment", "sentiment_shift", "price_change"]]
    y = df["trend_label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print(f"✅ Accuracy: {accuracy_score(y_test, preds):.2f}, F1: {f1_score(y_test, preds):.2f}, AUC: {roc_auc_score(y_test, preds):.2f}")

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/sentiment_model.pkl")
    print("✅ Model saved to models/sentiment_model.pkl")

if __name__ == "__main__":
    train_model()
