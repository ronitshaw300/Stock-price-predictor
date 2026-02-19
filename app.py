import os
import datetime
import numpy as np
import pandas as pd
import yfinance as yf
import google.generativeai as genai
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import streamlit as st

# -------------------- PAGE CONFIG -------------------- #
st.set_page_config(page_title="📈 AI Stock Predictor (India)", layout="wide")
st.title("📊 AI-Powered Indian Stock Price Predictor")

# -------------------- GEMINI SETUP -------------------- #
if "GEMINI_API_KEY" not in os.environ:
    api_key = st.sidebar.text_input("🔑 Enter your Gemini API key:", type="password")
    if api_key:
        os.environ["GEMINI_API_KEY"] = api_key
        genai.configure(api_key=api_key)
else:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# -------------------- USER INPUTS -------------------- #
st.sidebar.header("User Input")
stock_symbol = st.sidebar.text_input("Enter Indian Stock Symbol (e.g., RELIANCE.NS, TCS.NS):", "RELIANCE.NS")
start_date = st.sidebar.date_input("Start Date", datetime.date(2020, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime.date.today())
trend_input = st.sidebar.selectbox("Select Market Trend (Your View):", ("Bullish", "Bearish", "Neutral"))

# -------------------- MAIN FUNCTION -------------------- #
if st.sidebar.button("🔮 Predict"):
    with st.spinner("Fetching data, predicting, and analyzing..."):
        try:
            # -------------------- FETCH REAL DATA -------------------- #
            data = yf.download(stock_symbol, start=start_date, end=end_date)
            if data.empty:
                st.error("❌ No data found. Check the stock symbol or date range.")
                st.stop()

            data["Date"] = data.index
            data = data.reset_index(drop=True)

            # -------------------- TRAIN SIMPLE MODEL -------------------- #
            data["Day"] = np.arange(len(data))
            X = data[["Day"]]
            y = data["Close"].fillna(method="ffill")

            scaler = MinMaxScaler()
            y_scaled = scaler.fit_transform(np.array(y).reshape(-1, 1))

            model = LinearRegression()
            model.fit(X, y_scaled)

            # Predict next 15 days
            future_days = 30
            future_X = np.arange(len(X), len(X) + future_days).reshape(-1, 1)
            preds = model.predict(future_X)

            # Apply trend modification
            if trend_input == "Bullish":
                preds *= 1.05
            elif trend_input == "Bearish":
                preds *= 0.95

            preds = scaler.inverse_transform(preds)
            future_dates = pd.date_range(data["Date"].iloc[-1] + pd.Timedelta(days=1), periods=future_days)
            future_df = pd.DataFrame({"Date": future_dates, "Predicted Price": preds.flatten()})

            # -------------------- GRAPH (Historical + Predicted) -------------------- #
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(data["Date"], data["Close"], label="Historical Close Price", color="blue")
            ax.plot(future_df["Date"], future_df["Predicted Price"], label="Predicted Future Price", color="orange", linestyle="--")
            ax.set_title(f"{stock_symbol} - Price Prediction", fontsize=14)
            ax.set_xlabel("Date")
            ax.set_ylabel("Price (INR)")
            ax.legend()
            ax.grid(True)
            st.pyplot(fig)

            # -------------------- SHOW TABLE -------------------- #
            st.subheader(f"📅 Predicted Prices for {stock_symbol} (Next {future_days} Days)")
            st.dataframe(future_df)

            # -------------------- GEMINI AI ANALYSIS -------------------- #
            st.subheader("🤖 Gemini AI Market Analysis")

            prompt = f"""
You are a financial market expert.
Analyze the recent stock price trend for {stock_symbol} and its 15-day forecast.
The user perceives the market trend as '{trend_input}'.
Here are the last few closing prices: {data['Close'].tail(10).tolist()}.
Predicted prices for the next 15 days are: {future_df['Predicted Price'].tolist()}.

Provide a concise (around 150 words) analysis including:
1. Market sentiment
2. Buy / Sell / Hold suggestion
3. Risk factors and confidence in prediction.
"""


            model_ai = genai.GenerativeModel("gemini-1.5-flash")
            ai_response = model_ai.generate_content(prompt)

            st.write(ai_response.text)

        except Exception as e:
            st.error(f"❌ Error: {e}")

        # -------------------- SAVE MODEL & DATA -------------------- #
        try:
            import joblib
            joblib.dump(model, "stock_model.pkl")
            data.to_csv("stock_data.csv", index=False)
            st.success("✅ Model and data exported successfully for accuracy_check.py")
        except Exception as save_err:
            st.warning(f"⚠️ Could not save model/data: {save_err}")

st.sidebar.markdown("---")
st.sidebar.markdown("💡 **Tip:** 'Bullish' and 'Bearish' trends influence the prediction scaling.")
