from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'mysystem/login.html')

def registration(request):
    return render(request,'mysystem/registration.html')       