from .views import *
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('' , views.home ,name="home" ),
    path('login/', views.login_view ,name="login" ),
    path('register/', views.login_view ,name="register" ),
    path('add-blog', views.add_blog ,name="add_blog" ),
    
]
    