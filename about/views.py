from django.shortcuts import render

def about(request):

    if request.method == 'GET':
        return render (request, 'about.html')
    
    else:
        return render (request, 'about.html')

