from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin


class MXGSMonitoredHousekeepingTM(models.Model):
    utc_year_hk_gen                 =models.IntegerField()
    utc_msec_hk_gen                 =models.IntegerField()
    utc_seconds_hk_gen              =models.IntegerField()
    alive_counter                   =models.IntegerField()
    boot_complete                   =models.IntegerField()
    boot_status_completed_with_errors = models.BooleanField()
    boot_status_completed_no_errors = models.BooleanField()
    boot_status_asw_load_ok         = models.BooleanField()
    boot_status_system_memory_test_ok = models.BooleanField()
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
    sw_submode                      = models.CharField(max_length=2,
                                      choices=SW_SUBMODE_CHOICES,
                                      default=UNDEFINED)
    err_war_invalid_startcycle      = models.BooleanField()  # No valid or more than one valid Start Cycle Request TC packet is received by MMIA before the next TCP.
    err_war_nonscience_tm_discarded = models.BooleanField()  # Non-science downlink buffer is full
    err_war_comm_protocol           = models.BooleanField()  # Communication protocol error detected, will attempt to resynchonize protocol.
    err_war_invalid_EDLF_frame      = models.BooleanField() # Invalid EDLF frame received.
    err_war_task_deadline_missed    = models.BooleanField() # Task deadline missed or task queue full.
    err_war_software_exception      = models.BooleanField() # Software exception occured in Boot Software.
    err_war_nvm_powered_on          = models.BooleanField()
    psu_cont_tmon_chan1             = models.IntegerField()
    psu_cont_tmon_chan2             = models.IntegerField()
    dpu_int_tmon_1_fpga             = models.IntegerField()
    dpu_int_tmon_2_dcdc             = models.IntegerField()
    discarded_normal_packets        = models.IntegerField()
    ram_lhp_evap_tmon2              = models.IntegerField()
    wake_lhp_evap_tmon3             = models.IntegerField()
    led_count_ratemeter             = models.IntegerField()
    hed_count_ratemeter             = models.IntegerField()
    discarded_nonscience_packets    = models.IntegerField()
    recd_packets_count              = models.IntegerField()
    psu_cont_tmon_chan1_add         = models.IntegerField()
    psu_cont_tmon_chan2_add         = models.IntegerField()
    dpu_int_tmon_1_fpga_add         = models.IntegerField()
    dpu_int_tmon_2_dcdc_add         = models.IntegerField()
    psu_tmon_dau_czt_1_dcdc         = models.IntegerField()
    psu_tmon_dau_czt_2_dcdc         = models.IntegerField()
    psu_tmon_dau_czt_3_dcdc         = models.IntegerField()
    psu_tmon_dau_czt_4_dcdc         = models.IntegerField()
    psu_tmon_dau_bgo_1_dcdc         = models.IntegerField()
    psu_tmon_dau_bgo_2_dcdc         = models.IntegerField()
    psu_tmon_dau_bgo_3_dcdc         = models.IntegerField()
    psu_tmon_dau_bgo_4_dcdc         = models.IntegerField()
    dau_czt_1_tmon_chan2            = models.IntegerField()
    dau_czt_2_tmon_chan2            = models.IntegerField()
    dau_czt_3_tmon_chan2            = models.IntegerField()
    dau_czt_4_tmon_chan2            = models.IntegerField()
    dau_bgo_1_tmon_chan2            = models.IntegerField()
    dau_bgo_2_tmon_chan2            = models.IntegerField()
    dau_bgo_3_tmon_chan2            = models.IntegerField()
    dau_bgo_4_tmon_chan2            = models.IntegerField()
