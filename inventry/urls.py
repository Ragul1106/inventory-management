from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('in-stock/', views.in_stock, name='in_stock'),
    path('out-of-stock/', views.out_of_stock, name='out_of_stock'),
]