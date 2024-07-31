#THIS PROGRAM USES FINNHUB API TO PULL STOCK DATA FOR APPLE.
#FINNHUB PROVIDES FREE API KEY WHICH WILL BE REQUIRED TO RUN THIS PROGRAM.


import finnhub
import pandas as pd

# Set up the Finnhub client with your API key
finnhub_client = finnhub.Client(api_key="YOUR API KEY FOR FINNHUB")

# Thie line of code makes a request to get company basic financials
company_basic_financials = finnhub_client.company_basic_financials('AAPL', "all")


# This line of code checks if the response contains the 'metric' data
if 'metric' in company_basic_financials and company_basic_financials['metric']:
    metrics_data = company_basic_financials['metric']
    
    # This line of code convert the metrics data to a DataFrame
    df = pd.DataFrame([metrics_data])
    
    if 'Ticker' not in df.columns:
        df['Ticker'] = 'AAPL'
    
    df = df[['Ticker'] + [col for col in df.columns if col != 'Ticker']]

    # Saves an Excel file to a specific directory
    df.to_excel("C:\\Users\\deval\\OneDrive\\Desktop\\Company-financials.xlsx", index=False)

    print("Stock data is successfully exported to Company-financials.xlsx")
else:
    print("No 'metric' data found in the response.")

