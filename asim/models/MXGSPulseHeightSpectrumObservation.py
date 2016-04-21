from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin


# Pulse Height Spectrum Observation
class MXGSPulseHeightSpectrumObservation(models.Model):
    utc_year                        =models.IntegerField('UTC year')
    utc_msec                        =models.IntegerField('UTC msec')
    utc_seconds                     =models.IntegerField('UTC seconds')
    tcp_count_dhpu                  =models.IntegerField()
    tcp_count_dpu                   =models.IntegerField()
    start_dau_bgo_1_int_tmon_chan1  =models.IntegerField()
    start_dau_bgo_1_int_tmon_chan2  =models.IntegerField()
    start_dau_bgo_1_int_tmon_chan3  =models.IntegerField()
    start_dau_bgo_1_int_tmon_chan4  =models.IntegerField()
    start_dau_bgo_2_int_tmon_chan1  =models.IntegerField()
    start_dau_bgo_2_int_tmon_chan2  =models.IntegerField()
    start_dau_bgo_2_int_tmon_chan3  =models.IntegerField()
    start_dau_bgo_2_int_tmon_chan4  =models.IntegerField()
    start_dau_bgo_3_int_tmon_chan1  =models.IntegerField()
    start_dau_bgo_3_int_tmon_chan2  =models.IntegerField()
    start_dau_bgo_3_int_tmon_chan3  =models.IntegerField()
    start_dau_bgo_3_int_tmon_chan4  =models.IntegerField()
    start_dau_bgo_4_int_tmon_chan1  =models.IntegerField()
    start_dau_bgo_4_int_tmon_chan2  =models.IntegerField()
    start_dau_bgo_4_int_tmon_chan3  =models.IntegerField()
    start_dau_bgo_4_int_tmon_chan4  =models.IntegerField()
    integration_period              =models.IntegerField()
    CZT4 = 'CZ'
    BGO12 = 'BG'
    DATA_PROVIDED_CHOICES = (
        (CZT4, "4 CZT spectra"),
        (BGO12, "12 BGO spectra"),
    )
    data_provided = models.CharField(max_length=2,
                                      choices=DATA_PROVIDED_CHOICES,
                                      default=CZT4)
    czt_dau_pulse_height_spectra    =models.FileField()
    bgo_dau_pulse_height_spectra    =models.FileField()
    end_dau_bgo_1_int_tmon_chan1    =models.IntegerField()
    end_dau_bgo_1_int_tmon_chan2    =models.IntegerField()
    end_dau_bgo_1_int_tmon_chan3    =models.IntegerField()
    end_dau_bgo_1_int_tmon_chan4    =models.IntegerField()
    end_dau_bgo_2_int_tmon_chan1    =models.IntegerField()
    end_dau_bgo_2_int_tmon_chan2    =models.IntegerField()
    end_dau_bgo_2_int_tmon_chan3    =models.IntegerField()
    end_dau_bgo_2_int_tmon_chan4    =models.IntegerField()
    end_dau_bgo_3_int_tmon_chan1    =models.IntegerField()
    end_dau_bgo_3_int_tmon_chan2    =models.IntegerField()
    end_dau_bgo_3_int_tmon_chan3    =models.IntegerField()
    end_dau_bgo_3_int_tmon_chan4    =models.IntegerField()
    end_dau_bgo_4_int_tmon_chan1    =models.IntegerField()
    end_dau_bgo_4_int_tmon_chan2    =models.IntegerField()
    end_dau_bgo_4_int_tmon_chan3    =models.IntegerField()
    end_dau_bgo_4_int_tmon_chan4    =models.IntegerField()
