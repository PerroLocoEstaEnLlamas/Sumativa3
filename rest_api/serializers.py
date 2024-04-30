from rest_framework import serializers
from core.models import Juego
from core.models import Persona

class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = ['id_juego', 'nombre', 'precio', 'imagen']


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

      