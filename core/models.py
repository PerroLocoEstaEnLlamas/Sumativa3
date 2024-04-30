from django.db import models

# Create your models here.

class User(models.Model):
    usuario =models.CharField(max_length= 10, primary_key=True,verbose_name='Nombre Usuario')
    email = models.CharField(max_length=40, verbose_name='Email')
    clave = models.CharField(max_length=30, verbose_name='Clave')
    edad = models.CharField(max_length=3, verbose_name='Edad')
    pais = models.CharField(max_length=15, verbose_name='Pais')

    def __str__(self):
        return self.usuario
    
class Juego(models.Model):
    id_juego = models.CharField(max_length=3, unique=True)
    nombre= models.CharField(max_length=100)
    precio = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to= 'juegos/', null= True, blank = True)

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    usuario = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    clave = models.CharField(max_length=40)
    edad = models.CharField(max_length=3)
    pais = models.CharField(max_length=20)  
                