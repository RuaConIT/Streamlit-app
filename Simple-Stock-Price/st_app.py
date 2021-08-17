import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
    # Simple Stock Price App

Shown are the **stock** closing price and volume of google 

""")
TickerData = yf.Ticker("AAPL")

TickerDf = TickerData.history(period='1d', start='2010-5-31', end='2010-5-31')

st.line_chart(TickerDf.Close)
st.line_chart(TickerDf.Volume)