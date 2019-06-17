from django.db import models

# Create your models here.


class Movie(models.Model):
    uid = models.CharField(max_length=10)
    name = models.CharField(max_length=128)
    info = models.CharField(max_length=256)


class Jd(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()