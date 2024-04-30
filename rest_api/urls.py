from django.urls import path, include
from . import views

from django.contrib import admin

from .views import verificar_usuario




urlpatterns= [
    path('juegos/', views.lista_juegos, name= 'lista_juegos'),
    path('personas/', views.lista_personas, name= 'lista_personas'),
    path('verificar_usuario/', views.verificar_usuario, name='verificar_usuario'),
     path('forgot_password/', views.forgot_password, name='forgot_password'), 
]