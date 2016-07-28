from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin

class MXGSEnableInstrumentEvent (models.Model):
    command_length                        = models.IntegerField()
    no_events                        = models.IntegerField()
    generation_control  = models.IntegerField()
