from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin

class MXGSCommandVerificationReportTM(models.Model):
    packet_length                   = models.IntegerField('Packet length')
    tc_header                   = models.IntegerField()
    result   = models.IntegerField()
