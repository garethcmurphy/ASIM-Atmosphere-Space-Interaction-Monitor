from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin

class MXGSInstrumentSummaryHousekeepingTM (models.Model):
    packet_length                   =models.IntegerField()
    utc_year                        =models.IntegerField()
    utc_msec                        =models.IntegerField()
    utc_seconds                     =models.IntegerField()
    tcp_count_dhpu                  =models.IntegerField()
    tcp_count_dpu                   =models.IntegerField()
    err_war_invalid_startcycle      = models.BooleanField()  # No valid or more than one valid Start Cycle Request TC packet is received by MMIA before the next TCP.
    err_war_nonscience_tm_discarded = models.BooleanField()  # Non-science downlink buffer is full
    err_war_comm_protocol           = models.BooleanField()  # Communication protocol error detected, will attempt to resynchonize protocol.
    err_war_invalid_EDLF_frame      = models.BooleanField() # Invalid EDLF frame received.
    err_war_task_deadline_missed    = models.BooleanField() # Task deadline missed or task queue full.
    err_war_software_exception      = models.BooleanField() # Software exception occured in Boot Software.
    err_war_nvm_powered_on          = models.BooleanField()
 
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
    discarded_nonscience_packets    = models.IntegerField()
    dpu_count_prereset              = models.IntegerField()
    recd_packets_count              = models.IntegerField()
    discarded_normal_packets        = models.IntegerField()
    inst_summary_hk                 = models.BooleanField()  
    startup_hk                      = models.BooleanField()  
    buffer_resource_hk              = models.BooleanField()  
    ratemeter_hk                    = models.BooleanField()  
    dpu_hk                          = models.BooleanField()  
    czt_dau_summary_hk              = models.BooleanField()  
    czt_dau_1_full_hk               = models.BooleanField()  
    czt_dau_2_full_hk               = models.BooleanField()  
    czt_dau_3_full_hk               = models.BooleanField()  
    czt_dau_4_full_hk               = models.BooleanField()  
    bgo_dau_summary_hk              = models.BooleanField()  
    bgo_dau_1_full_hk               = models.BooleanField()  
    bgo_dau_2_full_hk               = models.BooleanField()  
    bgo_dau_3_full_hk               = models.BooleanField()  
    bgo_dau_4_full_hk               = models.BooleanField()  
    psu_hk                          = models.BooleanField()  
    enable_event_30000              = models.BooleanField()  
    enable_event_30010              = models.BooleanField()  
    enable_event_30090              = models.BooleanField()  
    enable_event_30100              = models.BooleanField()  
    enable_event_30110              = models.BooleanField()  
    enable_event_30120              = models.BooleanField()  
    enable_event_30130              = models.BooleanField()  
    enable_event_30140              = models.BooleanField()  
    enable_event_30160              = models.BooleanField()  
    enable_event_40000              = models.BooleanField()  
    enable_event_40010              = models.BooleanField()  
    enable_event_40020              = models.BooleanField()  
    enable_event_40030              = models.BooleanField()  
    enable_event_40040              = models.BooleanField()  
    enable_event_40050              = models.BooleanField()  
    enable_event_40090              = models.BooleanField()  
    enable_event_40100              = models.BooleanField()  
    enable_event_40110              = models.BooleanField()  
    enable_event_40120              = models.BooleanField()  
    enable_event_40150              = models.BooleanField()  
    enable_event_40160              = models.BooleanField()  
    enable_event_40170              = models.BooleanField()  
    enable_event_40180              = models.BooleanField()  
    enable_event_40190              = models.BooleanField()  
    enable_event_40200              = models.BooleanField()  
    enable_event_40210              = models.BooleanField()  
    enable_event_40260              = models.BooleanField()  
    enable_event_40270              = models.BooleanField()  
    enable_event_40280              = models.BooleanField()  
    enable_event_40290              = models.BooleanField()  
    dau_czt_1_lv                    = models.BooleanField()  
    dau_bgo_1_lv                    = models.BooleanField()  
    dau_czt_2_lv                    = models.BooleanField()  
    dau_bgo_2_lv                    = models.BooleanField()  
    dau_czt_3_lv                    = models.BooleanField()  
    dau_bgo_3_lv                    = models.BooleanField()  
    dau_czt_4_lv                    = models.BooleanField()  
    dau_bgo_4_lv                    = models.BooleanField()  
    dau_czt_1_lv                    = models.BooleanField()  
    dau_bgo_1_hv                    = models.BooleanField()  
    dau_czt_2_hv                    = models.BooleanField()  
    dau_bgo_2_hv                    = models.BooleanField()  
    dau_czt_3_hv                    = models.BooleanField()  
    dau_bgo_3_hv                    = models.BooleanField()  
    dau_czt_4_hv                    = models.BooleanField()  
    dau_bgo_4_hv                    = models.BooleanField()  
    led_count_ratemeter             = models.IntegerField()
    hed_count_ratemeter             = models.IntegerField()
    dau_total_rate                  = models.IntegerField()
    dau_data_reduc_factor           = models.IntegerField()
    buffer_detect_events            = models.IntegerField()
    discard_detect_events           = models.IntegerField()
    tgf_int_trigs                   = models.IntegerField()
    trigs_to_mmia                   = models.IntegerField()
    trigs_from_mmia                 = models.IntegerField()
    priority_1_obs_cap_cnt          = models.IntegerField()
    priority_2_obs_cap_cnt          = models.IntegerField()
    priority_3_obs_cap_cnt          = models.IntegerField()
    priority_1_obs_dlink_cnt        = models.IntegerField()
    priority_2_obs_dlink_cnt        = models.IntegerField()
    priority_3_obs_dlink_cnt        = models.IntegerField()
    dpu_int_tmon_1_dpu_fpga         = models.IntegerField()
    dpu_ext_tmon_2_ram_lhp          = models.IntegerField()
    dpu_ext_tmon_3_wake_lhp         = models.IntegerField()
    dpu_ext_tmon_5_dpu_trp          = models.IntegerField()
    dau_czt_1_tmon_chan2            = models.IntegerField()
    dau_czt_2_tmon_chan2            = models.IntegerField()
    dau_czt_3_tmon_chan2            = models.IntegerField()
    dau_czt_4_tmon_chan2            = models.IntegerField()
    dau_bgo_1_tmon_chan2            = models.IntegerField()
    dau_bgo_1_tmon_adc_ref_volt     = models.IntegerField()
    dau_bgo_2_tmon_chan2            = models.IntegerField()
    dau_bgo_2_tmon_adc_ref_volt     = models.IntegerField()
    dau_bgo_3_tmon_chan2            = models.IntegerField()
    dau_bgo_3_tmon_adc_ref_volt     = models.IntegerField()
    dau_bgo_4_tmon_chan2            = models.IntegerField()
    dau_bgo_4_tmon_adc_ref_volt     = models.IntegerField()
    psu_cont_tmon_chan1             = models.IntegerField()
    psu_cont_tmon_chan2             = models.IntegerField()
    lhp_countdown_time             = models.IntegerField()


