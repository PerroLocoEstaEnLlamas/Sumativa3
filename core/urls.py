from django.contrib import admin
from django.urls import path
#from . import views
from .views import home, perfil, login, carrito, olvido, registro

urlpatterns = [
    # Usar una cadena vacía para que sea la URL de inicio.
    path('', home, name='home'),
    path('perfil/',perfil, name='perfil'),
    path('login/', login, name='login'),
    path('carrito/', carrito, name='carrito'),
    path('olvido/', olvido, name='olvido'),
    path('registro/',registro, name='registro'),
]
