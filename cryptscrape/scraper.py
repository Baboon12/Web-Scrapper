from datetime import datetime
from operator import index
from traceback import print_tb
from urllib import response

import pandas as pd
import requests
from bs4 import BeautifulSoup

# Storing website name as a variable

website = 'https://coinmarketcap.com/'

# Requesting the website
response = requests.get(website)

# Getting the status code to see if it responds with 200OK
response.status_code
print(response.status_code)

# Creating the Soup Object for getting access to the html elements of website
soup = BeautifulSoup(response.content, 'html.parser')
# response.content to get the content of the response page
# html.parser is the parser of html page

# Storing results
results = soup.find(
    'table', {'class': 'cmc-table'}).find('tbody').find_all('tr')
# The data we need is stored in tr of tbody of table which has a class of table-scrollable.

# print(len(results))

# print(results[0].find('p', {'class': 'sc-1eb5slv-0 iworPT'}).get_text().strip())

# print(results[0].find('div', {'class': 'sc-131di3y-0 cLgOOr'}).get_text().strip())

# print(results[0].find('span', {'class': 'sc-15yy2pl-0 kAXKAX'}).get_text().strip())

# print(results[0].find('span', {'class': 'sc-15yy2pl-0 hzgCfk'}).get_text().strip())

# print(results[0].find('span', {'class': 'sc-1ow4cwt-1 ieFnWP'}).get_text().strip())

# print(results[0].find('p', {'class': 'sc-1eb5slv-0 hykWbK font_weight_500'}).get_text().strip())

# print(results[0].find('td', {'class': 'td-market_cap'}).get_text().strip())

# creating empty lists to append all our data
crypto_name = []
crypto_price = []
crypto_1h_change = []
crypto_24h_change = []
crypto_7d_change = []
crypto_volume_24h = []
# crypto_market_cap = [];

# Appending data to respective lists
for i in results:
    # name
    try:
        crypto_name.append(i.find('p', {'class': 'sc-1eb5slv-0 iworPT'}).get_text().strip())
    except:
        crypto_name.append('N/A')

    # price
    try:
        crypto_price.append(i.find('div', {'class': 'sc-131di3y-0 cLgOOr'}).get_text().strip())
    except:
        crypto_price.append('N/A')

#     # 1h change
    try:
        crypto_1h_change.append(i.find('span', {'class': 'sc-15yy2pl-0'}).get_text().strip())
    except:
        crypto_1h_change.append('N/A')

#     # 24h change
    try:
        crypto_24h_change.append(i.find('span', {'class': 'sc-15yy2pl-0'}).get_text().strip())
    except:
        crypto_24h_change.append('N/A')

    # 7d change
    try:
        crypto_7d_change.append(i.find('span', {'class': 'sc-1ow4cwt-1 ieFnWP'}).get_text().strip())
    except:
        crypto_7d_change.append('N/A')

    # 24h volume
    try:
        crypto_volume_24h.append(i.find('p', {'class': 'sc-1eb5slv-0 hykWbK font_weight_500'}).get_text().strip())
    except:
        crypto_volume_24h.append('N/A')

# # market capital
# # try:
# #     crypto_market_cap.append(i.find('td', {'class': 'td-market_cap'}).get_text().strip())
# # except:
# #     print('N/A');

# print(/crypto_price)

# # Setting pandas dataframe
# # Dataframe takes as input a dictionary whose
# #  1st parameter is Name of Column and
# #  2nd parameter is the dictionary that it takes data from
crypto_data_frame = pd.DataFrame({'Coin': crypto_name, 'Price': crypto_price, '1h_Change': crypto_1h_change, '24h_Change': crypto_24h_change, '7d_Change': crypto_7d_change, '24h_Volume': crypto_volume_24h})

# # output of dataframe
# print(len(crypto_data_frame))

dt = datetime.now()
ds = str(dt);   
dss = ds[0:10]
print(dss)
i=0;

print("H")
# output in excel file
crypto_data_frame.to_csv(dss+'_'+str(i)+'.csv', index=False)
i=i+1