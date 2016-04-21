
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin



class BackgroundObservation(models.Model):
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
    led_short_win_lr_pulse_height   =models.IntegerField()
    led_short_win_upr_pulse_height  =models.IntegerField()
    led_long_win_lr_pulse_height    =models.IntegerField()
    led_long_win_upr_pulse_height   =models.IntegerField()
    hed_short_win_lr_pulse_height   =models.IntegerField()
    hed_short_win_upr_pulse_height  =models.IntegerField()
    hed_long_win_lr_pulse_height    =models.IntegerField()
    hed_long_win_upr_pulse_height   =models.IntegerField()
    led_short_win_anticoin_time     =models.IntegerField()
    led_long_win_anticoin_time      =models.IntegerField()
    hed_short_win_anticoin_time     =models.IntegerField()
    hed_long_win_anticoin_time      =models.IntegerField()
    led_bin0_lr_boundary            =models.IntegerField()
    led_bin1_lr_boundary            =models.IntegerField()
    led_bin2_lr_boundary            =models.IntegerField()
    led_bin3_lr_boundary            =models.IntegerField()
    led_bin4_lr_boundary            =models.IntegerField()
    led_bin5_lr_boundary            =models.IntegerField()
    led_bin6_lr_boundary            =models.IntegerField()
    led_bin7_lr_boundary            =models.IntegerField()
    led_bin8_lr_boundary            =models.IntegerField()
    led_bin9_lr_boundary            =models.IntegerField()
    led_bin9_upr_boundary           =models.IntegerField()
    hed_bin0_lr_boundary            =models.IntegerField()
    hed_bin1_lr_boundary            =models.IntegerField()
    hed_bin2_lr_boundary            =models.IntegerField()
    hed_bin3_lr_boundary            =models.IntegerField()
    hed_bin4_lr_boundary            =models.IntegerField()
    hed_bin5_lr_boundary            =models.IntegerField()
    hed_bin6_lr_boundary            =models.IntegerField()
    hed_bin7_lr_boundary            =models.IntegerField()
    hed_bin8_lr_boundary            =models.IntegerField()
    hed_bin9_lr_boundary            =models.IntegerField()
    hed_bin9_upr_boundary           =models.IntegerField()
    led_short_win_dur_1             =models.IntegerField()
    led_short_win_dur_2             =models.IntegerField()
    led_short_win_dur_3             =models.IntegerField()
    led_long_win_dur                =models.IntegerField()
    hed_short_win_dur_1             =models.IntegerField()
    hed_short_win_dur_2             =models.IntegerField()
    hed_short_win_dur_3             =models.IntegerField()
    hed_long_win_dur                =models.IntegerField()


class BackgroundObservation1Second(models.Model):
    background_observation = models.ForeignKey(BackgroundObservation, on_delete=models.CASCADE)
    utc_year                        =models.IntegerField('UTC year')
    utc_seconds                     =models.IntegerField('UTC seconds')
    utc_msec                        =models.IntegerField('UTC msec')
    tcp_count_dhpu                  =models.IntegerField()
    tcp_count_dpu                   =models.IntegerField()
    dpu_count_prereset              =models.IntegerField()
    UNDEFINED = 'UD'
    CONFMODE  = 'CF'
    OPMODE   = 'OP'
    SW_MODE_CHOICES = (
        (UNDEFINED , "Undefined"            ),
        (CONFMODE  , "Configuration mode"   ),
        (OPMODE    , "Operational mode"     ),
    )
    sw_mode = models.CharField(max_length=2,
                                      choices=SW_MODE_CHOICES,
                                      default=UNDEFINED)
    UNDEFINED                       = 'UD'
    TGFSEARCH                       = 'TG'
    HIGHBACKGROUND                  = 'HB'
    AURORALCAPTURE                  = 'AC'
    SW_SUBMODE_CHOICES = (
        (UNDEFINED     , "Undefined"        ),
        (TGFSEARCH     , "TGF Search mode"  ),
        (HIGHBACKGROUND, "High Background"  ),
        (AURORALCAPTURE, "Auroral capture"  ),
    )
    sw_submode = models.CharField(max_length=2,
                                      choices=SW_SUBMODE_CHOICES,
                                      default=UNDEFINED)
    dau_data_reduc_factor           =models.IntegerField()
    led_count_ratemeter             =models.IntegerField()
    hed_count_ratemeter             =models.IntegerField()
    dau_total_rate                  =models.IntegerField()
    led_accept_count_rate_short     =models.IntegerField()
    led_accept_count_rate_long      =models.IntegerField()
    hed_accept_count_rate_short     =models.IntegerField()
    hed_accept_count_rate_long      =models.IntegerField()
    led_calc_background_rate_short  =models.IntegerField()
    led_calc_background_rate_long   =models.IntegerField()
    hed_calc_background_rate_short  =models.IntegerField()
    hed_calc_background_rate_long   =models.IntegerField()
    led_short_win_thresh_1          =models.IntegerField()
    led_short_win_thresh_2          =models.IntegerField()
    led_short_win_thresh_3          =models.IntegerField()
    led_long_win_thresh             =models.IntegerField()
    hed_short_win_thresh_1          =models.IntegerField()
    hed_short_win_thresh_2          =models.IntegerField()
    hed_short_win_thresh_3          =models.IntegerField()
    hed_long_win_thresh             =models.IntegerField()
    dau1_dm_if_1_current_offset     =models.IntegerField()
    dau1_dm_if_2_current_offset     =models.IntegerField()
    dau1_dm_if_3_current_offset     =models.IntegerField()
    dau1_dm_if_4_current_offset     =models.IntegerField()
    dau2_dm_if_1_current_offset     =models.IntegerField()
    dau2_dm_if_2_current_offset     =models.IntegerField()
    dau2_dm_if_3_current_offset     =models.IntegerField()
    dau2_dm_if_4_current_offset     =models.IntegerField()
    dau3_dm_if_1_current_offset     =models.IntegerField()
    dau3_dm_if_2_current_offset     =models.IntegerField()
    dau3_dm_if_3_current_offset     =models.IntegerField()
    dau3_dm_if_4_current_offset     =models.IntegerField()
    dau4_dm_if_1_current_offset     =models.IntegerField()
    dau4_dm_if_2_current_offset     =models.IntegerField()
    dau4_dm_if_3_current_offset     =models.IntegerField()
    dau4_dm_if_4_current_offset     =models.IntegerField()
    dau1_pmt_if_1_current_offset    =models.IntegerField()
    dau1_pmt_if_2_current_offset    =models.IntegerField()
    dau1_pmt_if_3_current_offset    =models.IntegerField()
    dau2_pmt_if_1_current_offset    =models.IntegerField()
    dau2_pmt_if_2_current_offset    =models.IntegerField()
    dau2_pmt_if_3_current_offset    =models.IntegerField()
    dau3_pmt_if_1_current_offset    =models.IntegerField()
    dau3_pmt_if_2_current_offset    =models.IntegerField()
    dau3_pmt_if_3_current_offset    =models.IntegerField()
    dau4_pmt_if_1_current_offset    =models.IntegerField()
    dau4_pmt_if_2_current_offset    =models.IntegerField()
    dau4_pmt_if_3_current_offset    =models.IntegerField()
    led_pulse_height_bin            =ArrayField( models.IntegerField(), size=10,)
    hed_pulse_height_bin            =ArrayField( models.IntegerField(), size=10,)
    led_time_bin_values             =ArrayField( models.IntegerField(), size=31,)
    hed_time_bin_values             =ArrayField( models.IntegerField(), size=31,)
    
    
