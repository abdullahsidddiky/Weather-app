from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
def index(request):
    ce0c01bdbd2978586a06f55294ccd379
    url = 'https://api.openweathermap.org/data/2.5/weather?q={Dhaka}&appid={ce0c01bdbd2978586a06f55294ccd379}'

    print(url)
    return render(request,'weather/index.html')
