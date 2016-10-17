from django.conf.urls import url
from django.contrib import admin
from .views import about, home

urlpatterns = [
	url(r'^about/$', about, name='about'),
    url(r'.*', home, name='home'),  
]
