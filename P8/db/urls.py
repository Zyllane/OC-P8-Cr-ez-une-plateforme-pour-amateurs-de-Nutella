from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_register', views.user_register, name='user_register'),
    path('user_login', views.user_login, name='user_login'),
    path('search_product', views.search_product, name='search_product')
]