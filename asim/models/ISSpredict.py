from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin


# Create your models here.


class ISSpredict(models.Model):
    userselect=models.IntegerField('User')
    lat=models.FloatField('Latitude')
    lon=models.FloatField('Longitude')
