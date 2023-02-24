from about.views import about
from django.urls import path


urlpatterns = [
    path('', about, name='about'),

    
]