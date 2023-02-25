from django.shortcuts import render
import requests

def index(request):
    api_key = '6284481ecd2c40ad955ad3b2873a2a73'
    url = 'https://newsapi.org/v2/top-headlines?country=br&category=health&apiKey=' + api_key
    response = requests.get(url)
    articles = response.json()['articles']
     
    context = {
        'articles': articles
    }

    return render (request, 'index.html', context)


