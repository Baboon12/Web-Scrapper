from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("login2",views.login2,name="login"),
    # path("login",views.login ,name="login"),
    # path("login2",views.login2,name="login2")
]
