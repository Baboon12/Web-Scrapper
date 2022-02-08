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

print(results[0].find('a', {'class': 'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text())

print(results[0].find('span', {'class': 'no-wrap'}).get_text())
