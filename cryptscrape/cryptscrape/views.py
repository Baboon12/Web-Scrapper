import imp
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
import mimetypes
import os
from datetime import datetime
from operator import index
from traceback import print_tb
from urllib import response

import pandas as pd
import requests
from bs4 import BeautifulSoup
from django.contrib import messages

# from .models import MyModel
# from .forms import MyForm

from scraper import scrapeSite


def index(request):
    return render(request, 'index.html')


def forgot(request):
    return render(request, 'forgot.html')

def logout(request):
    auth.logout(request);
    return redirect('/')
    
def login(request):
    #return render(request,'login.html')
    print('HUA')
    if request.method=='POST':
    
        username=request.POST['username'] 
        password=request.POST['pass']
        
        x = auth.authenticate(username=username,password=password)
        
        if x is not None:
            auth.login(request,x)
            return redirect('/')
        else:
            messages.info(request,'invalid cred')
            return redirect('login')
        
        
    else:
        return render(request,'login.html')

def otp(request):
    return render(request, 'otp.html')


def scraper(request):
    return render(request, 'scraper.py')


# def signup(request):
#     # return render(request, 'signup.html') fname lname email phone password
#     if request.method=='POST':
#         first_name=request.POST['fname']
#         last_name=request.POST['lname']
#         email=request.POST['email']
        
#         password=request.POST['pass']
        

#         user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
#         # user.save()
#         print('user created')
#         return redirect('/')
#     else:
#         return render(request,'signup.html')

def signup(request):
    print('hua')
    # return render(request,'signup.html')
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        # phone=request.POST['phone']
        password=request.POST['pass']
        username=request.POST['username']
        # phone=request.POST['phone']

        # user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        user.save()
        print('user created')
        return HttpResponseRedirect('/login')
    else:
        return render(request,'signup.html')
    
def output(request):

    output_data = scrapeSite()

    return render(request, "index.html", {"output_data": output_data})


# def my_form(request):
#     if request.method == "POST":
#         form = MyForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             form = MyForm()
#     return render(request, 'cv-form.html', {'form': form})

j = 0


def download_file(request):

    # scraper script:
    website = 'https://www.coingecko.com/'
    global j 

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
    results = soup.find(
        'table', {'class': 'table-scrollable'}).find('tbody').find_all('tr')
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
    crypto_name = []
    crypto_price = []
    crypto_1h_change = []
    crypto_24h_change = []
    crypto_7d_change = []
    crypto_volume_24h = []
    crypto_market_cap = []

    # Appending data to respective lists
    for i in results:
        # name
        try:
            crypto_name.append(i.find('a', {
                               'class': 'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip())
        except:
            print('N/A')

        # price
        try:
            crypto_price.append(i.find(
                'td', {'class': 'td-price price text-right pl-0'}).get_text().strip()).sort()
        except:
            print('N/A')

        # 1h change
        try:
            crypto_1h_change.append(
                i.find('td', {'class': 'td-change1h'}).get_text().strip())
        except:
            print('N/A')

        # 24h change
        try:
            crypto_24h_change.append(
                i.find('td', {'class': 'td-change24h'}).get_text().strip())
        except:
            print('N/A')

        # 7d change
        try:
            crypto_7d_change.append(
                i.find('td', {'class': 'td-change7d'}).get_text().strip())
        except:
            print('N/A')

        # 24h volume
        try:
            crypto_volume_24h.append(
                i.find('td', {'class': 'td-liquidity_score'}).get_text().strip())
        except:
            print('N/A')

        # market capital
        try:
            crypto_market_cap.append(
                i.find('td', {'class': 'td-market_cap'}).get_text().strip())
        except:
            print('N/A')

    # Setting pandas dataframe
    # Dataframe takes as input a dictionary whose
    #  1st parameter is Name of Column and
    #  2nd parameter is the dictionary that it takes data from
    crypto_data_frame = pd.DataFrame({'Coin': crypto_name, 'Price': crypto_price, '1h_Change': crypto_1h_change, '24h_Change': crypto_24h_change,
                                     '7d_Change': crypto_7d_change, '24h_Volume': crypto_volume_24h, 'Market_Capital': crypto_market_cap})

    # output of dataframe
    # print(crypto_data_frame)

    dt = datetime.now()
    ds = str(dt)
    dss = ds[0:10]
    print(dss)

    Excel_filename = dss+'_'+str(j)+'.csv'
    
    j =  j+1

    # output in excel file
    crypto_data_frame.to_csv(Excel_filename, index=False)

    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = Excel_filename
    # Define the full file path
    filepath = BASE_DIR + '\\' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response
