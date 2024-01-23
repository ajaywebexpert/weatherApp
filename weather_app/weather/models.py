from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

class WeatherSearch(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    conditions = models.CharField(max_length=255)
    forecast = models.TextField()
