import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from datetime import date, timedelta
import streamlit as st

st.title("Real-time Stock Price Data")
a = st.text_input("Enter Any Company Ticker Symbol:")

today = date.today()
d1 = today.strftime("%Y-%m-%d")
end_date = d1

d2 = date.today() - timedelta(days=365)
start_date = d2

try:
    st.write("Stock Symbol:", a)  # Print the stock symbol being used
    st.write("Start Date:", start_date) # Print the date you want to start looking at
    st.write("End Date:", end_date) # Print the final date you want to look at

    data = yf.download(a, start=start_date, end=end_date)

    if data.empty:
        st.write("No data available for the specified company or date range.")
    else:
        st.write(data.head())  # Print the first few rows of data for inspection
        fig, ax = plt.subplots()
        data["Close"].plot(figsize=(12, 8), title=a + " Stock Prices", fontsize=20, label="Close Price", ax=ax)
        plt.legend()
        plt.grid()
        st.pyplot(fig)
except Exception as e:
    st.write("Error occurred:", e)