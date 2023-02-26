from django.shortcuts import render, redirect
import requests
from index.forms import *

def index(request):

    if request.method == 'GET':
        api_key = '6284481ecd2c40ad955ad3b2873a2a73'
        url = 'https://newsapi.org/v2/top-headlines?country=br&category=health&apiKey=' + api_key
        response = requests.get(url)
        articles = response.json()['articles']
        
        context = {
            'articles': articles,
            'form':email(),
        }

        return render (request, 'index.html', context)
    
    else:
        form_email = email(request.POST)

        if form_email.is_valid():
            form_email.save()
            
        
        return redirect('index')

    
    



