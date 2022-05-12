"""cryptscrape URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from cgitb import html
from django import http
from django.http import HttpResponse
from django.shortcuts import render
import requests
import datetime
from .scraper import *
# import scrape


urlpatterns = [
    
    path('admin/', admin.site.urls),
    # path('scrapyfinal/',include('scrapyfinal.urls')),
    # path('loginscrape/',include('loginscrape.urls')),
    path('',views.index,name='index'),
    path('forgot',views.forgot,name='forgot'),
    path('otp',views.otp,name='otp'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('scraper',views.scraper,name='scraper'),
    # path('$',views.scraper),
    path('output',views.output,name="script"),
    path('download', views.download_file),
    path('downloadgeck', views.download_file_geck),
    path('downloadcap', views.download_file_cap),
    path('feedback',views.feedback)
]

# urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    # path('output',views.output,name="script"),

