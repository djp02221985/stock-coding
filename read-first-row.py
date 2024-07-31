#THIS PROGRAM READS DATA FROM AN EXCEL SHEET AND PRINTS ROW DATA IN THE COMMAND PROMPT. THIS WILL PRINT THE 60 TICKERS THAT ARE IN THE FIRST ROW.

import pandas as pd

# Load the Excel file
file_path = 'C:/Users/deval/OneDrive/Documents/TICKERS.xlsx'  # Replace with your file path
df = pd.read_excel(file_path, header=None)  # Read the file without a header

# Extract tickers from the first row
first_row_tickers = df.iloc[0].dropna().tolist()  # Drop NaN values and convert to list

# Print or use the tickers as needed
print("Tickers from the first row:")
print(first_row_tickers)


