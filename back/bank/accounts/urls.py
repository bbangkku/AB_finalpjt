from django.contrib import admin
from django.urls import path, include
from rest_framework import urls
from . import views
app_name = 'accounts'


urlpatterns = [
    path('delete/', views.user_delete,), # 회원탈퇴
    path("user/change/", views.userchange, name='user-change'), # 유저 변경
    path("user/product/put/", views.userproductput, name='user-put'), # 유저가입 상품 넣기
    path("user/product/delete/", views.userproductdelete, name='user-delete'), # 유저가입 상품 빼기
    path("user/get/<str:user_pk>/", views.getuser, name="getuser"),
    path('user/<str:user_pk>/recommend/', views.userrecommend), # 사용자 상품 추천(k-means)
]