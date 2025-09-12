from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required = True, validators = [validate_password])

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'nombre', 'apellido', 'rol', 'password')

    def create(self, validated_data):
        user = CustomUser(
            username = validated_data['username'],
            email = validated_data['email'],
            nombre = validated_data['nombre'],
            apellido = validated_data['apellido'],
            rol = validated_data['rol']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user