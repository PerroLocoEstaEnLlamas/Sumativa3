import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User
from .forms import LoginForm, UserForm

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def carrito(request):
    return render(request, 'core/carrito.html')

def olvido(request):
    return render(request, 'core/olvido.html')

#perfil usuario
def perfil(request):
    # Verifica si el usuario ha iniciado sesión
    if 'usuario_autenticado' in request.session and request.session['usuario_autenticado']:
        # Obtener los datos del usuario de la sesión
        usuario_id = request.session['usuario_id']
        usuario_nombre = request.session['usuario_nombre']
        usuario = User.objects.get(pk=usuario_id)
        return render(request, 'core/perfil.html', {'usuario': usuario})
    else:
        # Muestra un mensaje indicando que el usuario no ha iniciado sesión
        messages.warning(request, 'No has iniciado sesión. Por favor, inicia sesión para acceder a tu perfil.')
        return render(request, 'core/perfil.html')  

#Registro
def registro(request):
    datos = {
        'form': UserForm()
    }
    if request.method == 'POST':
        formulario = UserForm(request.POST, request.FILES)
        print("Contenido de request.FILES:", request.FILES)
        print("Contenido de request.POST:", request.POST)
        if formulario.is_valid(): 
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"
    return render(request, 'core/registro.html', datos)


#Login
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            clave = form.cleaned_data['clave']
            # Verifica si el usuario existe en la base de datos
            try:
                user = User.objects.get(email=email, clave=clave)
                
                request.session['usuario_autenticado'] = True
                request.session['usuario_id'] = user.pk
                request.session['usuario_nombre'] = user.usuario
                return render(request, 'core/login.html', {'form': form, 'show_welcome_alert': True})
            except User.DoesNotExist:
               
                pass
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form, 'show_welcome_alert': False})



