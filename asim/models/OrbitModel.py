from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin


# Create your models here.

class OrbitModel(models.Model):
    night=models.BooleanField()
    orbitstr=models.CharField(max_length=200)
