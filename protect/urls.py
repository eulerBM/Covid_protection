from protect.views import protect
from django.urls import path


urlpatterns = [
    path('', protect, name='protect' ),
]
