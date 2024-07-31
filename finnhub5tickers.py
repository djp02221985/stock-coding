#THIS PROGRAM FETCHES STOCK DATA FOR 5 TICKERS, PROCESSES IT, AND EXPORTS IT OT AN EXCEL SHEET.

import finnhub
import pandas as pd

# This line of code sets up the Finnhub client using personal API key
finnhub_client = finnhub.Client(api_key="YOUR API KEY FOR FINNHUB")


tickers = ['AAPL', 'TSLA', 'MSFT', 'AMZN', 'META']

# This is an empty list the will hold the stock data
data = []

try:
    for ticker in tickers:
        # This line of code get the basic financial data for all tickers
        company_basic_financials = finnhub_client.company_basic_financials(ticker, 'all')

        
        if 'metric' in company_basic_financials: # Checks for data availability.
            metric_data = company_basic_financials['metric']
            
            # Add 'Ticker' to metric data dictionary
            metric_data['Ticker'] = ticker
            
            # Append metric data dictionary to the list
            data.append(metric_data)
            print("Data fetched successfully for" + ticker + ".")
        else:
            print("Error: No metric data found for" + ticker + ".")
    # Convert list of dictionaries to DataFrame
    df = pd.DataFrame(data)
    
    # This line of code puts Ticker names in the first column.
   #df = df[['Ticker'] + [col for col in df.columns if col != 'Ticker']]
   
    columns = ['Ticker']
    for col in df.columns:
            if col != 'Ticker':
                columns.append(col)
    df = df[columns]
    
    # This line of code exports DataFrame to an Excel file named ticker-data.xlsx.
    df.to_excel("ticket-data.xlsx", index=False)
    print("Data exported successfully to ticker-data.xlsx")
    
#Exception handling 
except finnhub.exceptions.FinnhubAPIException as e:
    print("Finnhub API Exception:" + {e} + ".")
except Exception as e:
    print("Error fetching data:" + {e} + ".")
