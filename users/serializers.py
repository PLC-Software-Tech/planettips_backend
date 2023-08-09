from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.get('password')
        hashed_password = make_password(password)
        validated_data['password'] = hashed_password
        return super().create(validated_data)

    def update(self, instance, validated_data):
        password = validated_data.get('password')
        if password:
            hashed_password = make_password(password)
            validated_data['password'] = hashed_password
        return super().update(instance, validated_data)
    
    def get_groups(self, user):
        return user.groups.values_list('name', flat=True)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ['email', 'password']
 


class AppVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppVersion
        fields = '__all__'