from django.db import models
from django.urls import reverse



class Book (models.Model):
    NAME_ROOM = models.CharField(max_length=50)
    COLICHESTVO = models.CharField(max_length=50)
    PRICE = models.IntegerField(default=0)

class Menu (models.Model):
    TITLE = models.CharField(max_length=50)
    NOMERA= models.CharField(max_length=50)
    GLAV_STRANICA = models.CharField(max_length=50)

class Hotel (models.Model):
    CLASS_NOMER = models.CharField(max_length=50)
    CLASS = models.CharField(max_length=50)
    TV = models.BooleanField(default=True)
    IMG = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    Booked = models.BooleanField(default='Бронирование')