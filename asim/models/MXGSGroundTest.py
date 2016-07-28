from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin

class MXGSGroundTest (models.Model):
    private_header  = models.IntegerField()
    command_length  = models.IntegerField()
    action_id  = models.IntegerField()
