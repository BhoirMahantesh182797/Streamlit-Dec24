import streamlit as st
import yfinance as yf
import datetime

st.title("Stock Analyser")
col1, col2, col3 = st.columns(3)

with col1:

    stock_name = st.text_input('Which stock you want to analyse','GOOG')

ticker_data = yf.Ticker(stock_name)

with col2:

    start_date = st.date_input('Please Enter Start Date', datetime.date(2023, 12, 1))

with col3:

     End_date = st.date_input('Please Enter End Date', datetime.date(2024, 12, 1))

Timeframe = st.text_input('Timeframe','1d')

ticker_df = ticker_data.history(period = Timeframe, start = start_date, end = End_date)

st.subheader('Stock Information')
st.dataframe(ticker_df.head())

st.subheader('Price movement overtime')
st.line_chart(ticker_df['Close'])

st.subheader('Volume movement overtime')
st.line_chart(ticker_df['Volume'])