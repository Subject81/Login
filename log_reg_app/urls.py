from django.urls import path
from . import views

urlpatterns =[
    path('',views.index),
    path('user',views.index),
    path('new',views.new),
    path('create',views.create),
    path('welcome',views.welcome),
    path('registration',views.registration),
    path('login', views.login),
    path('logout', views.logout),
]