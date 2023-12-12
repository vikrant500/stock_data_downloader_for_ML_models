import requests
from datetime import datetime
import time
from art_psdp import logo

print(logo)

print("\nHere is a list of companies whose public stocks you may access:\nApple\nSamsung\nMicrosoft\nGoogle\nTesla\n")

company = input("please enter the name of the company whose public stocks you would like to download: \n").lower()

# Getting the ticker symbol for the brand
def get_ticker():

    run_code = 1

    if company == "apple":
        ticker = "AAPL"
        return ticker

    elif company == "samsung":
        ticker = "SSNLF"
        return ticker

    elif company == "microsoft":
        ticker = "MSFT"
        return ticker

    elif company == "Google":
        ticker = "GOOG"
        return ticker

    elif company == "Tesla":
        ticker = "TSLA"
        return ticker

    else:
        print("Invalid response")
        run_code = 0
        return run_code
    
# if the input company is valid, rest of the program runs

if get_ticker != 0:

    # getting the time_period of the stocks from the user
    from_date = input('Enter start date in yyyy/mm/dd format:')
    to_date = input('Enter end date in yyyy/mm/dd format:')

    # converting the date and time to the format recognized by the browser
    from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
    to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

    from_epoch = int(time.mktime(from_datetime.timetuple()))
    to_epoch = int(time.mktime(to_datetime.timetuple()))

    # taking data from the web
    url = f"https://query1.finance.yahoo.com/v7/finance/download/{get_ticker()}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

    content = requests.get(url, headers=headers).content
    
    # downloading the data in a '.csv' type format
    with open('data.csv', 'wb') as file:
        file.write(content)