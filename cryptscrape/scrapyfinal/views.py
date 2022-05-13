# # from django.shortcuts import render
# from contextlib import nullcontext
# from email import message
# from tkinter import E
# from django.contrib.auth.models import User,auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib.auth.models import User,auth
# import mimetypes
# import os
# from datetime import datetime
# from operator import index
# from traceback import print_tb
# from urllib import response

# Create your views here.


def login2(request):
    
    username=request.POST['username']
    password=request.POST['pass']
        
    


def signup(request):
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
    
def login(request):
    #return render(request,'login.html')
    if request.method== 'POST':
        # pass
        username=request.POST['username'] 
        password=request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/index')
        else:
            # messages.info(request,'invalid cred')
            return HttpResponseRedirect('login')
        print('HUA')
        
    else:
        return HttpResponseRedirect('login')
    
    
     
