from bs4 import BeautifulSoup
import requests

try:
    
    url = 'https://finviz.com/screener.ashx'

    # Set the headers to include the User-Agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Make the GET request with headers
    source = requests.get(url, headers=headers)
    source.raise_for_status()  # Check for errors

    #This line of code parses the HTML content using BeautifulSoup
    soup = BeautifulSoup(source.text, 'html.parser')
    # Print the formatted HTML content. Navigate and inspect through the pasred content and helps locate specific elements.
    print(soup.prettify())  

except Exception as e:
    print(e)