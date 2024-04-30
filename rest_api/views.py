from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from rest_framework.response import Response

from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.views.decorators.csrf import csrf_protect
from core.models import Juego,Persona
from .serializers import JuegoSerializer, PersonaSerializer
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
import requests



@csrf_exempt
@api_view (['GET', 'POST'])
def lista_juegos(request):
    if request.method == 'GET':
        juego = Juego.objects.all()
        serializer = JuegoSerializer(juego, many=True)
        
        return Response(serializer.data)


@csrf_exempt
@api_view(['GET', 'POST'])  
def lista_personas(request):
    if request.method == 'GET':
        persona = Persona.objects.all()
        serializer = PersonaSerializer(persona, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)
    
from django.http import JsonResponse
from django.contrib.auth.models import User

@csrf_protect
@api_view(['GET','POST'])
def verificar_usuario(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        clave = request.POST.get('clave')
        usuario = authenticate(request, username=email, password=clave)
        if usuario is not None:
            login(request, usuario)  
            return redirect('/perfil/')  
        else:
            
            return redirect('/login/')

@csrf_exempt
@api_view(['GET', 'POST']) 
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        api_url = 'http://127.0.0.1:8000/api/personas/'
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            email_exists = any(person['email'] == email for person in data)
            if email_exists:
                message = "Mensaje de recuperación enviado."
            else:
                message = "El usuario no existe. Intente nuevamente."
        else:
            message = "Error en la solicitud."

        return JsonResponse({'message': message})

