#This is the code to test the availability of pre-market, intraday, and post-market stock data from Finnhub.
#I ran this code at different times of the day to get pre-market, intraday, and post-market data. Finnhub does not provide pre-market data if you have free membership.
#This program uses Quote API to get data that are updated daily such as c- close price, d- daily volume, dp - daily percentage change in stock price,
# h - high price during traing day, l- low price during trading day, and o- price when the market opens.

import finnhub              
import pandas as pd

# Initialize the Finnhub client
finnhub_client = finnhub.Client(api_key="YOUR API KEY")

quote = finnhub_client.quote('AAPL')

print(quote)

# This converts quote data into pandas dataframe
quote_dataframe = pd.DataFrame([quote])

# Add the 'Ticker' column
quote_dataframe['Ticker'] = 'AAPL'

quote_dataframe = quote_dataframe[['Ticker'] + [col for col in quote_dataframe.columns if col != 'Ticker']]
#filename = 'finnhub-after-hours.xlsx'

# This line of code exports the DataFrame to an Excel file
quote_dataframe.to_excel("finnhub-testing.xlsx", index=False)

print("Data is successfully exported to finnhub-testing.xlsx.")
  