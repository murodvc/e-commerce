from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from app.views import customers, customers_details, add_customer, edit_customer, delete_customers, login, register

urlpatterns = [
    path('', customers, name='customers'),
    path('customer-detail/<slug:slug>/',customers_details, name='customer_detail'),
    path('add-customer/', add_customer, name='add_customer'),
    path('edit_customer/<int:pk>/',edit_customer, name='edit_customer'),
    path('customer-detail/<int:pk>/delete-customer/',delete_customers, name='delete_customer'),
    path('login/',login, name='login'),
    path('register/',register, name='register'),

]