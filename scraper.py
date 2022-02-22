
from traceback import print_tb
from urllib import response

import pandas as pd
import requests
from bs4 import BeautifulSoup

# Storing website name as a variable
website = 'https://www.coingecko.com/'

# Requesting the website
response = requests.get(website)

# Getting the status code to see if it responds with 200OK
response.status_code
# print(response.status_code)

# Creating the Soup Object for getting access to the html elements of website
soup = BeautifulSoup(response.content, 'html.parser')
# response.content to get the content of the response page
# html.parser is the parser of html page

# Storing results
results = soup.find('table', {'class': 'table-scrollable'}).find('tbody').find_all('tr')
# The data we need is stored in tr of tbody of table which has a class of table-scrollable.

# print(len(results))

# print(results[0].find('a', {'class': 'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip())

# print(results[0].find('td', {'class': 'td-price price text-right pl-0'}).get_text().strip())

# print(results[0].find('td', {'class': 'td-change1h'}).get_text().strip())

# print(results[0].find('td', {'class': 'td-change24h'}).get_text().strip())

# print(results[0].find('td', {'class': 'td-change7d'}).get_text().strip())

# print(results[0].find('td', {'class': 'td-liquidity_score'}).get_text().strip())

# print(results[0].find('td', {'class': 'td-market_cap'}).get_text().strip())

# creating empty lists to append all our data
crypto_name = [];
crypto_price = [];
crypto_1h_change = [];
crypto_24h_change = [];
crypto_7d_change = [];
crypto_market_cap = [];

# Appending data to respective lists
for i in results:
    # name
    try:
        crypto_name.append(i.find('a', {'class': 'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip())
    except:
        print('N/A');
    
    # price
    try:
        crypto_price.append(i.find('td', {'class': 'td-price price text-right pl-0'}).get_text().strip())
    except:
        print('N/A');
    
    # 1h change
    try:
        crypto_1h_change.append(i.find('td', {'class': 'td-change1h'}).get_text().strip())
    except:
        print('N/A');
    
    # 24h change
    try:
        crypto_24h_change.append(i.find('td', {'class': 'td-change24h'}).get_text().strip())
    except:
        print('N/A');
    
    # 7d change
    try:
        crypto_7d_change.append(i.find('td', {'class': 'td-change7d'}).get_text().strip())
    except:
        print('N/A');
    
    # market capital
    try:
        crypto_market_cap.append(i.find('td', {'class': 'td-market_cap'}).get_text().strip())
    except:
        print('N/A');