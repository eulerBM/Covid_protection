from django.urls import path
from doctors.views import doctors


urlpatterns = [
    path('', doctors, name='doctors'),

   
]