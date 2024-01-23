from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import WeatherSearch
from .serializers import UserSerializer, WeatherSearchSerializer
import requests

User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)

class UserLoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class WeatherSearchView(generics.CreateAPIView):
    serializer_class = WeatherSearchSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        city = request.data.get('city')
        user = self.request.user

        # Use AccuWeather API to get weather information
        api_key = 'your_accuweather_api_key'
        url = f'http://dataservice.accuweather.com/locations/v1/cities/search'
        params = {'apikey': api_key, 'q': city}
        response = requests.get(url, params=params)
        data = response.json()

        if data:
            location_key = data[0]['Key']
            url = f'http://dataservice.accuweather.com/currentconditions/v1/{location_key}'
            params = {'apikey': api_key}
            response = requests.get(url, params=params)
            weather_data = response.json()[0]

            # Save search history to the database
            WeatherSearch.objects.create(
                user=user,
                city=city,
                temperature=weather_data['Temperature']['Metric']['Value'],
                conditions=weather_data['WeatherText'],
                forecast='No forecast available',  # You can extend this using a 5-day forecast API
            )

            return Response({'message': 'Weather search recorded successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'City not found'}, status=status.HTTP_404_NOT_FOUND)
