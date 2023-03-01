from django.shortcuts import render

def doctors(request):

    if request.method == 'GET':
        return render (request, 'doctors.html')

    else:
        return render (request, 'doctors.html')