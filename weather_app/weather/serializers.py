from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import WeatherSearch

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class WeatherSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherSearch
        fields = '__all__'
