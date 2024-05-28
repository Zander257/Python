from bs4 import BeautifulSoup as bs
import re as regularExpression
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

Tickers_list = []

def getTickers(text):
    pattern = r"\$([A-Za-z]{3,4}+)"
    tickers = regularExpression.findall(pattern, text)
    return tickers

def appendTickers(file_paths):
    for file_path in file_paths:
        with open(file_path, 'r', encoding="utf-8") as file:
            text = file.read()

        tickers = getTickers(text)
        Tickers_list.append(tickers)

def scrapeFile(file_paths, Tickers_list, interval):
    ticker_count = 0

    for file_path in file_paths:
        tickers = getTickers(file_path)
        if ticker in Tickers_list:
            ticker_count += 1

    print(f"{ticker} was mentioned {ticker_count} times in the last {interval} minutes.")

################################################################################################

# Provide the correct file paths
file_paths = [
    "C:/Users/zainm/OneDrive/Desktop/Twitter Scraper/Mr_Derivatives.txt", 
    "C:/Users/zainm/OneDrive/Desktop/Twitter Scraper/warrior_0719.txt",  
    "C:/Users/zainm/OneDrive/Desktop/Twitter Scraper/ChartingProdigy.txt",  
    "C:/Users/zainm/OneDrive/Desktop/Twitter Scraper/allstarcharts.txt",  
    "C:/Users/zainm/OneDrive/Desktop/Twitter Scraper/yuriymatso.txt",  
    "C:/Users/zainm/OneDrive/Desktop/Twitter Scraper/TriggerTrades.txt", 
    "C:/Users/zainm/OneDrive/Desktop/Twitter Scraper/AdamMancini4.txt",  
    "C:/Users/zainm/OneDrive/Desktop/Twitter Scraper/CordovaTrades.txt", 
    "C:/Users/zainm/OneDrive/Desktop/Twitter Scraper/Barchart.txt",  
    "C:/Users/zainm/OneDrive/Desktop/Twitter Scraper/RoyLMattox.txt",  
]

# Define the ticker symbol and interval
#ticker = "$TSLA"
interval = 15

# Call the scrapeFile function
for ticker in Tickers_list:
    scrapeFile(file_paths, ticker, interval)