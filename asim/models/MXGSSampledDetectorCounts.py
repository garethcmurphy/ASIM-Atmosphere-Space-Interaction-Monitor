from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin


class MXGSSampledDetectorCounts(models.Model):
    dau_bgo_1_int_tmon_chan1        =models.IntegerField()
    dau_bgo_1_int_tmon_chan2        =models.IntegerField()
    dau_bgo_1_int_tmon_chan3        =models.IntegerField()
    dau_bgo_1_int_tmon_chan4        =models.IntegerField()
    dau_bgo_2_int_tmon_chan1        =models.IntegerField()
    dau_bgo_2_int_tmon_chan2        =models.IntegerField()
    dau_bgo_2_int_tmon_chan3        =models.IntegerField()
    dau_bgo_2_int_tmon_chan4        =models.IntegerField()
    dau_bgo_3_int_tmon_chan1        =models.IntegerField()
    dau_bgo_3_int_tmon_chan2        =models.IntegerField()
    dau_bgo_3_int_tmon_chan3        =models.IntegerField()
    dau_bgo_3_int_tmon_chan4        =models.IntegerField()
    dau_bgo_4_int_tmon_chan1        =models.IntegerField()
    dau_bgo_4_int_tmon_chan2        =models.IntegerField()
    dau_bgo_4_int_tmon_chan3        =models.IntegerField()
    dau_bgo_4_int_tmon_chan4        =models.IntegerField()

class MXGSSampledDetectorCounts1Second(models.Model):
    mxgs_sampled_detector_counts = models.ForeignKey(MXGSSampledDetectorCounts, on_delete=models.CASCADE)
    utc_year                        =models.IntegerField('UTC year')
    utc_msec                        =models.IntegerField('UTC msec')
    utc_seconds                     =models.IntegerField('UTC seconds')
    tcp_count_dhpu                  =models.IntegerField()
    tcp_count_dpu                   =models.IntegerField()
    dpu_count_prereset              =models.IntegerField()
    dpu_count_Sample_Ratio          =models.IntegerField()
    grey_mode_data_reduc_factor     =models.IntegerField()
    detector_counts                 =models.IntegerField()
    detector_events                 =models.FileField()
