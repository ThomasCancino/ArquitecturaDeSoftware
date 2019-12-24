#Comunicador entre distintos tipos de datos cmo json 
from rest_framework import serializers
from django.contrib.auth.models import User 

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    ApellidoPaterno= serializers.CharField(max_length=35)
    ApellidoMaterno= serializers.CharField(max_length=35)
    Nombres = serializers.CharField(max_length=35)
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def NombreCompleto(self):
        cadena= "{0} {1},{2}"
        return cadena.format(self.ApellidoPaterno,self.ApellidoMaterno,self.Nombres)
    
    def __str__(self):
        return self.NombreCompleto()

    #validador de usuario 
    def create(self, validate_data):
        instance = User()
        instance.NombreCompleto = validate_data.get('NombreCompleto')
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, data):
        users = User.object.filter(username = data)
        if len(user) != 0: 
            raise serializers.ValidationError("Este nombre de usuario ya existe, ingrese uno nuevo")
        else: 
            return data