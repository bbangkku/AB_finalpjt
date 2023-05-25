from django.urls import path, include
from . import views

app_name = 'api'
urlpatterns = [
    path('deposit/', views.save_deposit_products),
    path('installment/', views.save_installment_products),
    path('d_detail/<str:product_id>/', views.d_detail),
    path('i_detail/<str:product_id>/', views.i_detail),
    
    
    
    
    path('addproduct/<str:user_pk>/<str:fin_prdt_cd>/', views.addproduct),
    # path('deleteproduct/<int:user_pk>/<str:fin_prdt_cd>/', views.deleteproduct),
    # path('subproduct/<str:product_id>/<str:username>', views.subscribe),
    path('likeproduct/<str:product_id>/', views.like),
    # path('userproductchange/<str:user_pk>',views.userproductchange)
]
