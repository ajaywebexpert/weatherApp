from django.urls import path
from .views import UserCreateView, UserLoginView, WeatherSearchView

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('weather/search/', WeatherSearchView.as_view(), name='weather-search'),
]
