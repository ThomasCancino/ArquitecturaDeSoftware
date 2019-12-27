from rest_framework import serializers
from .models import Persona
from  .prueba import prueba

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = (
            'id',
            'nombre',
            'apellido',
        )

class dataSerializer(serializers.ModelSerializer):

    class Meta: 
        model = prueba
        fields = '__all__'