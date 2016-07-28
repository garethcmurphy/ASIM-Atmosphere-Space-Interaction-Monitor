from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin


class MXGSBGODAUSummaryHousekeepingTM(models.Model):
    packet_length                   = models.IntegerField('Packet length')
    utc_year                        = models.IntegerField('UTC year')
    utc_msec                        = models.IntegerField('UTC msec')
    utc_seconds                     = models.IntegerField('UTC seconds')
    tcp_count_dpu                   = models.IntegerField()
    acquisition_start_time_current  = models.IntegerField()
    grey_mode_data_reduc_factor     = models.IntegerField()
    dau_bgo_1_ratemeter             = models.IntegerField()
    dau_bgo_1_tmon_chan_1           = models.IntegerField()
    dau_bgo_1_tmon_chan_2           = models.IntegerField()
    dau_bgo_1_internal_tmon_chan_1  = models.IntegerField()
    dau_bgo_1_internal_tmon_chan_2  = models.IntegerField()
    dau_bgo_1_internal_tmon_chan_3  = models.IntegerField()
    dau_bgo_1_tmon_ref_voltage      = models.IntegerField()
    dau_bgo_1_high_voltage_mon      = models.IntegerField()
    dau_bgo_2_ratemeter             = models.IntegerField()
    dau_bgo_2_tmon_chan_1           = models.IntegerField()
    dau_bgo_2_tmon_chan_2           = models.IntegerField()
    dau_bgo_2_internal_tmon_chan_1  = models.IntegerField()
    dau_bgo_2_internal_tmon_chan_2  = models.IntegerField()
    dau_bgo_2_internal_tmon_chan_3  = models.IntegerField()
    dau_bgo_2_tmon_ref_voltage      = models.IntegerField()
    dau_bgo_2_high_voltage_mon      = models.IntegerField()
    dau_bgo_3_ratemeter             = models.IntegerField()
    dau_bgo_3_tmon_chan_1           = models.IntegerField()
    dau_bgo_3_tmon_chan_2           = models.IntegerField()
    dau_bgo_3_internal_tmon_chan_1  = models.IntegerField()
    dau_bgo_3_internal_tmon_chan_2  = models.IntegerField()
    dau_bgo_3_internal_tmon_chan_3  = models.IntegerField()
    dau_bgo_3_tmon_ref_voltage      = models.IntegerField()
    dau_bgo_3_high_voltage_mon      = models.IntegerField()
    dau_bgo_4_ratemeter             = models.IntegerField()
    dau_bgo_4_tmon_chan_1           = models.IntegerField()
    dau_bgo_4_tmon_chan_2           = models.IntegerField()
    dau_bgo_4_internal_tmon_chan_1  = models.IntegerField()
    dau_bgo_4_internal_tmon_chan_2  = models.IntegerField()
    dau_bgo_4_internal_tmon_chan_3  = models.IntegerField()
    dau_bgo_4_tmon_ref_voltage      = models.IntegerField()
    dau_bgo_4_high_voltage_mon      = models.IntegerField()
    

