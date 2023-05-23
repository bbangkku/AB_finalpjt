from django.contrib import admin
from django.urls import path, include
from rest_framework import urls

app_name = 'accounts'


urlpatterns = [
    path("api-auth/", include('rest_framework.urls')),
]
