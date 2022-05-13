from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    if request.method=='POST':
        # pass
        username=request.POST['username']
        password=request.POST['password']
        
        
        # user = auth.authenticate(username=username,password=password)
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/index')
        else:
            # messages.info(request,'invalid cred')
            return redirect('login')
        print('HUA')
        
    else:
        return redirect('login')
