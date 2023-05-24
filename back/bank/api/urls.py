from django.urls import path, include
from . import views

app_name = 'api'
urlpatterns = [
    path('deposit/', views.save_deposit_products),
    path('installment/', views.save_installment_products),
    path('d_detail/<str:product_id>/', views.d_detail),
    path('i_detail/<str:product_id>/', views.i_detail),
    path('subproduct/<str:product_id>/', views.subscribe),
    path('likeproduct/<str:product_id>/', views.like),
    path('userproductchange/<str:user_pk>',views.userproductchange)
]
