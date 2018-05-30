from django.urls import path 
from second_app import views

urlpatterns = [
    path('', views.second_app, name='second_app'),
    path('help/', views.help, name='help'),
]
