#THIS IS COMPLETE PROGRAM TO READ FILE AND FETCH DATA FROM THE FINNHUB API. Finnhub has a limit of 60 API calls per minute.
#This program fetches data for S&P 500 companies and also handles 60 calls per minute limitation in place by Finnhub for free account. 

import requests
import finnhub         
import pandas as pd
import time

# Function to read tickers from an Excel sheet
def read_excel(file_path):
    df = pd.read_excel(file_path, header=None)  
    # This line of code fetches tickers from all 9 rows
    tickers = df.iloc[0:9].values.flatten().tolist()  
    return tickers

# To read tickers from Excel sheet
file_path = 'C:/Users/deval/OneDrive/Documents/TICKERS.xlsx'  
sp500_tickers = read_excel(file_path)

# This line of code sets up finnhub client with the API key
finnhub_client = finnhub.Client(api_key="cq5la21r01qhs6itpjk0cq5la21r01qhs6itpjkg")

ticker_data = []

counter = 0

try:
    for ticker in sp500_tickers:
        if pd.isnull(ticker):
            continue
        # Make a request to get company basic financials for each ticker
        company_basic_financials = finnhub_client.company_basic_financials(ticker, 'all')

        # Check if 'metric' data is available
        if 'metric' in company_basic_financials:
            metric_data = company_basic_financials['metric']
            
            # Add 'Ticker' to metric data dictionary
            metric_data['Ticker'] = ticker
            
            # Append metric data dictionary to the list
            ticker_data.append(metric_data)
            print(f"The ticker data was fetched successfully for {ticker}.")
        else:
            print(f"The data fetching was unsuccessful for {ticker}.")
            
     # Increment the counter
        counter += 1

        # Pause to respect rate limit
        if counter % 60 == 0:
            print("The program has paused to keep up with 60 API calls per minute requirement.")
            time.sleep(60)

except Exception as e:
    print(f"Could not fetch data due to error: {str(e)}")

# Convert list of ticker data into a pandas DataFrame
df = pd.DataFrame(ticker_data)

# Reorder columns (optional): Place 'Ticker' column first
#df = df[['Ticker'] + [col for col in df.columns if col != 'Ticker']]

df = df[[col for col in df.columns if not df[col].isnull().all()]]

# Print DataFrame to the console
print(df)

# Exports DataFrame to Excel file
df.to_excel("sp500_data.xlsx", index=False)
print("Data exported successfully to sp500_data.xlsx")

