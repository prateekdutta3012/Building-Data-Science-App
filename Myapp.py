#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install streamlit')


# In[3]:


get_ipython().system(' pip install yfinance')


# In[4]:


import yfinance as yf
import streamlit as st
import pandas as pd


# In[6]:


st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Google!
""")
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


# In[ ]:




