from django.urls import path, include
from . import views

app_name = 'api'
urlpatterns = [
    path('deposit/', views.save_deposit_products),
    path('installment/', views.save_installment_products),
    path('d_detail/<str:product_id>/', views.d_detail),
    path('i_detail/<str:product_id>/', views.i_detail),
]
