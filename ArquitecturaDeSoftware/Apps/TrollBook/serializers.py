#Comunicador entre distintos tipos de datos cmo json 
from rest_framework import serializers
from django.contrib.auth.models import User 

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    Apellidos= serializers.CharField()
    Nombres = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()


    #validador de usuario 
    def create(self, validate_data):
        instance = User()
        instance.Apellidos = validate_data.get('Apellidos')
        instance.Nombres = validate_data.get('Nombres')
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, data):
        users = User.objects.filter(username = data)
        if len(users) != 0: 
            raise serializers.ValidationError("Este nombre de usuario ya existe, ingrese uno nuevo")
        else: 
            return data

#creo un modelo de usuario para poder verlo en viewas 
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSerializer
        field = {
            'id',
            'Nombres',
            'Apellidos'
        }