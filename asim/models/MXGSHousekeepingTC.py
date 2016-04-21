from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin

class MXGSHousekeepingTC(models.Model):
    command_length                  =models.IntegerField()
    housekeeping_id                 =models.IntegerField()
    generation_control              =models.IntegerField()
    generation_period              =models.IntegerField()


