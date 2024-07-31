# stock-coding
This repository is for fetching stock data from finviz.com finnhub.com and Yahoo Finance

**FINVIZ**
There are three files in this repository that has code to fetch dat from finviz.com.
finviz.py and finviz-data.py

**finviz.py** This program is for web scraping data for all 9560 stock tickers from finviz screener.
I used Notepad++ text editor for coding and command prompt to run the program.
This program is written in Python programming language and the libraries used in this program include BeautifulSoup, requests, and openpyxl.

**To install these libraries enter the following commands in the command prompt:**
pip install beautifulsoup4
pip install requests
pip install openpyxl

**To run this code in command prompt:**
python finviz.py

**finviz-data.py** This program is used to web scrap and parse HTML content from finviz.com stock screener page. 
I used Notepad++ text editor for coding and command prompt to run the program.
This program is written in Python programming language and the libraries used in this program include BeautifulSoup and requests.

**To install these libraries enter the following commands in the command prompt:**
pip install beautifulsoup4
pip install requests

**To run this code in command prompt:**
python finviz-data.py


**Finnhub - Finnhub provides free API KEY to fetch data using APIs that are available on free account.**
There are 6 files that have programs to fetch stock data from Finnhub.

**1) finnhub-api.py** - This program uses Finnhub API to pull stock data for Apple.

I used Notepad++ text editor for coding and command prompt to run the program.
This program is written in Python programming language and the libraries used in this program include finnhub-python and pandas.

**To install these libraries enter the following commands in the command prompt:**
pip install finnhub-python
pip install pandas
pip install openpyxl (ONLY IF YOU GET AN ERROR RUNNIG THIS CODE.)

**To run this code in command prompt:**
python finnhub-api.py

**2) finnhub5tickers.py** - This program fetches data for 5 ticker: Apple, Tesla, Microsoft, Amazon, and Meta, provcesses the data, and exports the data to an Excel Sheet.

I used Notepad++ text editor for coding and command prompt to run the program.
This program is written in Python programming language and the libraries used in this program include finnhub and pandas.

**To install these libraries enter the following commands in the command prompt:**
pip install finnhub-python
pip install pandas

**To run this code in command prompt:**
python finnhub5tickers.py

**3)finnhubsp500.py** - This program uses web scrapping to get S&P 500 stock tickers from a website and then pulls stock data from Finnhub for all 500 tickets.

I used Notepad++ text editor for coding and command prompt to run the program.
This program is written in Python programming language and the libraries used in this program include finnhub, BeautifulSoup, pandas, and time (part of Python's standard library so you don't have to install it but import time in your program.

**To install these libraries enter the following commands in the command prompt:**
pip install beautifulsoup4
pip install requests
pip install finnhub-python
pip install pandas

**To run this code in command prompt:**
python finnhubsp500.py

**4)finnhub-different-time-testing.py** - This is the code to test the availability of pre-market, intraday, and post-market stock data from Finnhub. This program uses Quote API to get data that are updated daily such as c- close price, d- daily volume, dp - daily percentage change in stock price,
h - high price during traing day, l- low price during trading day, and o- price when the market opens.

I used Notepad++ text editor for coding and command prompt to run the program.
This program is written in Python programming language and the libraries used in this program include finnhub and pandas.

**To install these libraries enter the following commands in the command prompt:**
pip install finnhub-python
pip install pandas

**To run this code in command prompt:**
python finnhub-different-time-testing.py

**5) read-first-row.py** - This program reads data from an Excel sheet and prints row data in the command prompt. This will print the 60 tickers that are in the first row of the eXcel file named TICKERS.xlxs and it is available in thie repository.

I used Notepad++ text editor for coding and command prompt to run the program.
This program is written in Python programming language and the pandas library.

**To install pandas, enter the following command in the command prompt.**
pip install pandas

**To run this code in command prompt:**
python read-first-row.py

**6) read-file-finnhub.py** - This is a complete program to read an excel file and fetch data from Finnhub using Finnhub API. Finnhub's free membership account has a limit of 60 API calls per minute. This program fetches data for S&P 500 companies and also handles 60 calls per minute limitation.

I used Notepad++ text editor for coding and command prompt to run the program.
This program is written in Python programming language and the libraries used in this program include finnhub, pandas, requests, and time (part of Python's standard library so you don't have to install it but import time in your program).

**To install these libraries enter the following commands in the command prompt:**
pip install requests
pip install finnhub-python
pip install pandas

**To run this code in command prompt:**
python read-file-finnhub.py

**7) yfinance-data.py** - This program fetches data from Yahoo Finance using Python's yfinance library. This program fetches data for Apple stock only.

I used Notepad++ text editor for coding and command prompt to run the program.
This program is written in Python programming language. The Python libraries used include pandas and yfinance.

**To install these libraries enter the following commands in the command prompt:**
pip install yfinance
pip install pandas

**To run this code in command prompt:**
python yfinance-data.py









