from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin

class MXGSSensorSwitchOffTC   (models.Model):
    private_header  = models.IntegerField()
    command_length  = models.IntegerField()
    dau_czt_1_lv  = models.BooleanField()
    dau_bgo_1_lv  = models.BooleanField()
    dau_czt_2_lv  = models.BooleanField()
    dau_bgo_2_lv  = models.BooleanField()
    dau_czt_3_lv  = models.BooleanField()
    dau_bgo_3_lv  = models.BooleanField()
    dau_czt_4_lv  = models.BooleanField()
    dau_bgo_4_lv  = models.BooleanField()
    dau_czt_1_lv_hv  = models.BooleanField()
    dau_bgo_1_lv_hv  = models.BooleanField()
    dau_czt_2_lv_hv  = models.BooleanField()
    dau_bgo_2_lv_hv  = models.BooleanField()
    dau_czt_3_lv_hv  = models.BooleanField()
    dau_bgo_3_lv_hv  = models.BooleanField()
    dau_czt_4_lv_hv  = models.BooleanField()
    dau_bgo_4_lv_hv  = models.BooleanField()
