from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin

class MXGSCZTDAUFullHousekeepingTM (models.Model):
    utc_year                        = models.IntegerField('UTC year')
