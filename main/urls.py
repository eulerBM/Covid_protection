from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Index
    path('home/', include('index.urls')),

    # Protect
    path('protect/', include('protect.urls')),

    # News
    path('news/', include('news.urls')),

    # Doctors
    path('doctors/', include('doctors.urls')),

    # About
    path('about/', include('about.urls')),
]
