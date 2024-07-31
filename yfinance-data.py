#This is the code to fetch data using yfinance which is a Python library that fetches stock data from Yahoo Finance.
#This program fetches data for one ticker only that is Apple in this case.

import yfinance as yfin         
import pandas as pd

# Stock ticker for which data will be fetched
ticker = "AAPL"

# create stock ticker object
stock = yfin.Ticker(ticker)

# Fetch historical market data 
# You can specify the period you are interested in
# Common periods: "1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"
data = stock.history(interval="5m") #This line of code fetched data at an internal of 5 minutes for the current month from 9:30 am to 4 pm.

# Display the first few rows of the data
print(data.head())

# Remove timezone information from the index
data.index = data.index.tz_localize(None)

# This line of code saves data to an Excel file
data.to_excel(ticker +"_data.xlsx", index=True)
print("Data exported successfully to" + ticker +"_data.xlsx")
