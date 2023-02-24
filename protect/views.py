from django.shortcuts import render

def protect(request):
    return render (request, 'protect.html')
