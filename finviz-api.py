import requests

URL = "https://elite.finviz.com/export.ashx??v=111&f=exch_nasd,fa_div_o6&r=181&auth=f9723451-e5f4-4b31-ad6c-6fd253be9959" #NASDAQ WITH DIVIDEND OVER 6%

response = requests.get(URL)

if response.status_code == 200:

    with open("export.csv", "wb") as file: 
        file.write(response.content)
        
    print("Data exported successfully")
    
else:
   print("Operation was unsuccessful")  