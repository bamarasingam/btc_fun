import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import datetime

def fetch_data(symbol, start_date, end_date, interval):
    data = yf.Ticker(symbol)
    return data.history(start=start_date, end=end_date, interval=interval)

def plot_candlestick(data):
    candlestick = go.Candlestick(x=data.index,
                                  open=data['Open'],
                                  high=data['High'],
                                  low=data['Low'],
                                  close=data['Close'])
    layout = go.Layout(title=f'{symbol} Candlestick Chart',
                       xaxis=dict(title='Date', rangeslider=dict(visible=False)),
                       yaxis=dict(title='Price'),
                       xaxis_rangeslider_visible=True)
    fig = go.Figure(data=[candlestick], layout=layout)
    return fig

st.title('Cryptocurrency Price Candlestick Chart')

symbol = st.selectbox('Select Cryptocurrency', ['BTC-USD', 'ETH-USD', 'XRP-USD'])
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=365*5)  # 5 years back
interval = st.selectbox('Select Time Frame', ['1d', '4h'])

data = fetch_data(symbol, start_date, end_date, interval)

if not data.empty:
    st.plotly_chart(plot_candlestick(data))
else:
    st.error('Failed to fetch data. Please check the symbol and try again.')
