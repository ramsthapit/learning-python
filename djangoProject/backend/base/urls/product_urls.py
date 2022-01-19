from django.urls import path
from . import views


urlpatterns = [
    path('', views.getProducts, name='Products'),
    path('<str:pk>/', views.getProduct, name='Product'),
]
