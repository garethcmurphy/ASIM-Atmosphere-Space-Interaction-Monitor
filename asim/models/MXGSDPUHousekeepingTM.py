from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin

class MXGSDPUHousekeepingTM (models.Model):
    packet_length                   = models.IntegerField('Packet length')
    utc_year                        = models.IntegerField('UTC year')
    utc_msec                        = models.IntegerField('UTC msec')
    utc_seconds                     = models.IntegerField('UTC seconds')
    tcp_count_dpu                   = models.IntegerField()
    acquisition_start_time_current  = models.IntegerField()
    supply_voltage_1v               = models.IntegerField()
    supply_voltage_2_5v             = models.IntegerField()
    supply_voltage_3_3v             = models.IntegerField()
    supply_current_1v               = models.IntegerField()
    supply_current_2_5v             = models.IntegerField()
    supply_current_3_3v             = models.IntegerField()
    dpu_internal_tmon_1_fpga        = models.IntegerField()
    dpu_internal_tmon_2_dcdc        = models.IntegerField()
    dpu_external_tmon_1_starb_rad   = models.IntegerField()
    dpu_external_tmon_2_ram_lhp     = models.IntegerField()
    dpu_external_tmon_3_wake_lhp    = models.IntegerField()
    dpu_external_tmon_4_ram_rad     = models.IntegerField()
    dpu_external_tmon_5_dpu_trp     = models.IntegerField()
    dpu_external_tmon_6_wake_supp   = models.IntegerField()
    dpu_external_tmon_7_wake_collim = models.IntegerField()
    dpu_external_tmon_8_lower_box   = models.IntegerField()
    
