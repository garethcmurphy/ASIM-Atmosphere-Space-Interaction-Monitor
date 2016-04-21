from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin


class MXGSRatemeterHousekeeping (models.Model):
    utc_year                        = models.IntegerField('UTC year')
    utc_seconds                     = models.IntegerField('UTC seconds')
    utc_msec                        = models.IntegerField('UTC msec')
    tcp_count_dpu                   = models.IntegerField()
    acquisition_start_time_current  = models.IntegerField()
    dau_czt_1_ratemeter_count       = models.IntegerField()
    dau_czt_2_ratemeter_count       = models.IntegerField()
    dau_czt_3_ratemeter_count       = models.IntegerField()
    dau_czt_4_ratemeter_count       = models.IntegerField()
    dau_bgo_1_ratemeter_count       = models.IntegerField()
    dau_bgo_2_ratemeter_count       = models.IntegerField()
    dau_bgo_3_ratemeter_count       = models.IntegerField()
    dau_bgo_4_ratemeter_count       = models.IntegerField()
    led_count_ratemeter             = models.IntegerField()
    hed_count_ratemeter             = models.IntegerField()
    dau_total_rate                  = models.IntegerField()
    led_accept_count_rate_short     = models.IntegerField()
    led_accept_count_rate_long      = models.IntegerField()
    hed_accept_count_rate_short     = models.IntegerField()
    hed_accept_count_rate_long      = models.IntegerField()
    led_calc_background_rate_short  = models.IntegerField()
    led_calc_background_rate_long   = models.IntegerField()
    hed_calc_background_rate_short  = models.IntegerField()
    hed_calc_background_rate_long   = models.IntegerField()
    led_short_win_thresh_1          = models.IntegerField()
    led_short_win_thresh_2          = models.IntegerField()
    led_short_win_thresh_3          = models.IntegerField()
    led_long_win_thresh             = models.IntegerField()
    hed_short_win_thresh_1          = models.IntegerField()
    hed_short_win_thresh_2          = models.IntegerField()
    hed_short_win_thresh_3          = models.IntegerField()
    hed_long_win_thresh             = models.IntegerField()

