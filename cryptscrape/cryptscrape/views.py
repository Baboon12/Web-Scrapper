import email
import imp
from unicodedata import name
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
from django.contrib import messages

import pandas as pd
import requests
from bs4 import BeautifulSoup
from django.contrib import messages
from .models import feedback
from django.contrib.auth.models import AbstractUser
import sweetify

# from .models import MyModel
# from .forms import MyForm

# from scraper import scrapeSite


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


def feedback(request):
    # if request.method=="POST":
    #     if request.POST.get('name') and request.POST.get('email') and request.POST.get('feedback'): 
    print('aaya')
    # name=request.POST.get['name']
    # email=request.POST.get['email']
    # feed=request.POST.get['feedback']
    
    # feedback = feedback(name=name, email= email, feedback=feed)
    # feedback.save()
    if request.method=='POST':
        
        # last_name=request.POST['lname']
        email=request.POST['email']
        feedback=request.POST['feedback']
        # phone=request.POST['phone']
        # password=request.POST['pass']
        username=request.POST['username']
        # phone=request.POST['phone']

        # user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        user = User.objects.create_user(username=username,email=email,first_name=feedback)
        user.save()
        print('user created')
        return HttpResponseRedirect('/login')
    else:
        pass
    # saverecord=feedback(request)
    # saverecord.name=request.POST('name')
    # saverecord.email=request.POST.get('email')
    # saverecord.feedback=request.POST.get('feedback')
    # # saverecord.save
    # return render(request, 'index.html')
    # else:
    #     pass


# def signup(request):
#     # return render(request, 'signup.html') fname lname email phone password
#     if request.method=='POST':
#         first_name=request.POST['fname']g
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

    global j
    
    
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
    Excel_filename = dss+'_gecko_'+str(j)+'.csv'
    
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




def download_file_cap(request):

    global j
    
    
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
    Excel_filename = dss+'_cap_'+str(j)+'.csv'
    
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




def download_file_geck(request):

    global j
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
    crypto_volume_24h = [];
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

        # 24h volume
        try:
            crypto_volume_24h.append(i.find('td', {'class': 'td-liquidity_score'}).get_text().strip())
        except:
            print('N/A');
        
        # market capital
        try:
            crypto_market_cap.append(i.find('td', {'class': 'td-market_cap'}).get_text().strip())
        except:
            print('N/A');

    # Setting pandas dataframe
    # Dataframe takes as input a dictionary whose
    #  1st parameter is Name of Column and 
    #  2nd parameter is the dictionary that it takes data from
    crypto_data_frame = pd.DataFrame({'Coin': crypto_name, 'Price': crypto_price, '1h_Change': crypto_1h_change, '24h_Change': crypto_24h_change, '7d_Change': crypto_7d_change, '24h_Volume': crypto_volume_24h, 'Market_Capital': crypto_market_cap})

    # output of dataframe
    # print(crypto_data_frame)

    dt = datetime.now()
    ds = str(dt);
    dss = ds[0:10]
    print(dss)
    i=0;

    # output in excel file
    crypto_data_frame.to_csv(dss+'_'+str(i)+'.csv', index=False)
    i=i+1

    dt = datetime.now()
    ds = str(dt);   
    dss = ds[0:10]
    print(dss)
    i=0;

    print("H")
    # output in excel file
    crypto_data_frame.to_csv(dss+'_'+str(i)+'.csv', index=False)
    i=i+1
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



