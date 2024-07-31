#This program is for web scraping all 9560 stock tickers from finviz screener.
    
from bs4 import BeautifulSoup
import requests
import openpyxl

def fetch_data():
    try:
        # Create a new Excel file
        excel = openpyxl.Workbook()
        sheet = excel.active  # sheet is the default name of an excel sheet. This line makes the excel sheet active.
        sheet.title = 'Finviz Data'
        sheet.append(['Number', 'Ticker', 'Company', 'Sector', 'Industry', 'Country', 'Market Cap', 'P/E', 'Price', 'Change', 'Volume'])
            
        initial_url = 'https://finviz.com/screener.ashx?v=111'
        page = 1
        last_page_reached = False
            
        while not last_page_reached:
            if page == 1:
                url = initial_url
            if page == 9561:
                break
            else:
                url = f'{initial_url}&r={page}'
                
                # Set the headers to include the User-Agent
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
                
                # Make the GET request with headers
                source = requests.get(url, headers=headers)
                source.raise_for_status()  # Check for errors
                
                # Parse the HTML content using BeautifulSoup  
                soup = BeautifulSoup(source.text, 'html.parser')  
                
                table = soup.find('table', class_="styled-table-new is-rounded is-tabular-nums w-full screener_table")
                rows = table.find_all('tr', class_="styled-row is-hoverable is-bordered is-rounded is-striped has-color-text")
                
                if not rows:
                    last_page_reached = True
                    print("END END END")
                    break;
                else:
                    for row in rows:
                        cells = row.find_all('td')
                        if cells:
                        # Extract cell data
                            cell_data = [cell.text.strip() for cell in cells]
                        # Append to Excel sheet
                            sheet.append(cell_data)
                            print(cell_data)
                    # Increment page by 20 for the next set of rows
                    page += 20            
                
            
            # Save Excel file
            excel.save('Finviz Retrived Data.xlsx')
            print('Data extraction and saving complete.')
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_data()
    
