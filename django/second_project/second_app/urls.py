from django.urls import path 
from second_app import views

urlpatterns = [
    path('', views.second_app, name='second_app'),
    path('help/', views.help, name='help'),
    path('users/', views.users, name='users'),
    path('user_data/', views.user_data_input, name='user_data_input'),
]
