from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin

class MXGSLoadMemoryTC   (models.Model):
    private_header  = models.IntegerField()
    command_length  = models.IntegerField()
    memory_id  = models.IntegerField()
    start_address  = models.IntegerField()
    dump_data  = models.FileField()
