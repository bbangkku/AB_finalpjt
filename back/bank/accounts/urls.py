from django.contrib import admin
from django.urls import path, include
from rest_framework import urls
from . import views
app_name = 'accounts'


urlpatterns = [
    path('delete/', views.user_delete,), # 회원탈퇴
    path("user/change/", views.userchange, name='user-change'), # 유저 변경
    path("user/product/<str:user_pk>", views.userproductget, name='user-change'), # 유저가입 상품 조회
    path('user/<int:user_pk>/recommend/', views.userrecommend), # 사용자 상품 추천(k-means)
]