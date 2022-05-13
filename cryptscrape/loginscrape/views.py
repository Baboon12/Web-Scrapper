from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib.auth.models import User,auth
# Create your views here.
def login2(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        x=authenticate(username=username,password=password)
        if x is None:
            return redirect('login')
        else:
            return redirect('/index')
        
    else:
        return redirect('login')
    # return render(request,'login.html')