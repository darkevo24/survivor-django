from django.db import models

class Survivor(models.Model):
    name = models.CharField(max_length = 200)
    age = models.IntegerField()
    gender = models.CharField(max_length = 200)
    latitude = models.FloatField()
    longitude = models.FloatField()