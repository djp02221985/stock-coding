#THIS PROGRAM WEBS SCRAPPED S&P 500 STOCK TIKERS FROM A WEBSITE AND THEN SFETCHED STOCK DATA FROM fINNHUB FOR ALL 500 TICKERS. 
#This program factors for 60 API call limits per minute.

import requests
from bs4 import BeautifulSoup
import finnhub                            
import pandas as pd
import time

# Function to fetch S&P 500 tickers from Stock Analysis
def fetch_sp500_tickers():
    url = 'https://stockanalysis.com/list/sp-500-stocks/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the rows 
    table = soup.find('tbody')
    
    if table:
        rows = table.find_all('tr', class_='svelte-eurwtr')

        tickers = []
        for row in rows:
            # This looks for ticker symbol in each row
            symbol = row.find('td', class_='sym svelte-eurwtr')
            if symbol:
                tickers.append(symbol.text.strip())

        return tickers
    else:
        print("Table body not found in the HTML.")
        return []

# Pull S&P 500 stock tickers
sp500_tickers = fetch_sp500_tickers()

# Setting up finnhub client with the API key
finnhub_client = finnhub.Client(api_key="YOUR API KEY FOR FINNHUB")


stock_data = []

# Counter to keep track of the number of requests
counter = 0

try:
    for ticker in sp500_tickers:
        # Make a request to get company basic financials for each ticker
        company_basic_financials = finnhub_client.company_basic_financials(ticker, 'all') 

        # Check if 'metric' data is available
        if 'metric' in company_basic_financials:
            metric_data = company_basic_financials['metric']
            
            # Add 'Ticker' to metric data dictionary
            metric_data['Ticker'] = ticker
            
            # Append metric data dictionary to the list
            stock_data.append(metric_data)
            print("The ticker data was fetched successfully for " + ticker + ".")
        else:
            print("The data fetching was unsuccessful for " + ticker + ".")

        # Increment the counter
        counter += 1

        # Pause to respect rate limit
        if counter % 60 == 0:   
            print("The program has paused to keep up with 60 API calls per minute limitation.")
            time.sleep(60)

except Exception as e:
    print("Could not fetch data for " + ticker + " due to error: " + str(e))

# Convert list of dictionaries to DataFrame
df = pd.DataFrame(all_company_data)

# Reorder columns (optional): Place 'Ticker' column first
df = df[['Ticker'] + [col for col in df.columns if col != 'Ticker']]

# Export DataFrame to Excel file
df.to_excel("full_sp500_company_info.xlsx", index=False)
print("Data exported successfully to full_sp500_company_info.xlsx")

   
             
             

         
