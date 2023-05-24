from django.contrib import admin
from django.urls import path, include
from rest_framework import urls
from . import views
app_name = 'accounts'


urlpatterns = [
    path("user/change/<str:username>/", views.userchange, name='user-change'),
]