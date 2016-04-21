from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin

class MXGSStartupHousekeepingTM(models.Model):
    tcp_count_dpu                   = models.IntegerField()
    acquisition_start_time_current  = models.IntegerField()
    boot_status_completed_with_errors = models.BooleanField()
    boot_status_completed_no_errors = models.BooleanField()
    boot_status_asw_load_ok         = models.BooleanField()
    boot_status_system_memory_test_ok = models.BooleanField()
    boot_status_asw_load_ok         = models.BooleanField()
    boot_software_version_major     = models.IntegerField()
    boot_software_version_minor     = models.IntegerField()
    app_software_version_major      = models.IntegerField()
    app_software_version_minor      = models.IntegerField()
    app_software_version_patch      = models.IntegerField()


