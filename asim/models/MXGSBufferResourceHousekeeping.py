from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin


class MXGSBufferResourceHousekeeping (models.Model):
    utc_year                        = models.IntegerField('UTC year')
    utc_seconds                     = models.IntegerField('UTC seconds')
    utc_msec                        = models.IntegerField('UTC msec')
    tcp_count_dpu                   = models.IntegerField()
    acquisition_start_time_current  = models.IntegerField()
    nonscience_dlink_buffer_usage   = models.IntegerField()
    science_tm_dlink_buffer_usage   = models.IntegerField()
    priority_1_data_buffer_usage    = models.IntegerField()
    priority_2_data_buffer_usage    = models.IntegerField()
    priority_3_data_buffer_usage    = models.IntegerField()
    discard_tc_packet_count         = models.IntegerField()
    discard_nonscience_tm_count     = models.IntegerField()
    discard_priority_3_count        = models.IntegerField()
    discard_priority_2_count        = models.IntegerField()
    discard_priority_1_count        = models.IntegerField()

