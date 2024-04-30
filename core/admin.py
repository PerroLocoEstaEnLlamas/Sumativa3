from django.contrib import admin

from .models import Juego, User, Persona

# Register your models here.

admin.site.register(Juego)
admin.site.register(User)
admin.site.register(Persona)