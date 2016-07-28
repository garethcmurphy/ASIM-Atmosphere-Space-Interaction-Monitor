from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin

class MXGSCZT1DAUFullHousekeepingTM (models.Model):
    packet_length                   = models.IntegerField('Packet length')
    utc_year                        = models.IntegerField('UTC year')
    utc_msec                        = models.IntegerField('UTC msec')
    utc_seconds                     = models.IntegerField('UTC seconds')
    tcp_count_dpu                   = models.IntegerField()
    acquisition_start_time_current  = models.IntegerField()
    grey_mode_data_reduc_factor     = models.IntegerField()
    dau_czt_1_ratemeter_count       = models.IntegerField()
    dau_czt_1_tmon_channel_1        = models.IntegerField()
    dau_czt_1_tmon_channel_2        = models.IntegerField()
    dau_czt_1_high_voltage_mon      = models.IntegerField()
    dau_xa_cfg_1_cr0_start_readback = models.BooleanField()
    dau_xa_cfg_1_cr0_reset_status   = models.BooleanField()
    dau_xa_cfg_1_cr0_start_config   = models.BooleanField()
    dau_xa_cfg_1_cr1_serial_clock_div   = models.IntegerField()
    dau_xa_cfg_1_cr2_err_inj_mask_1  = models.BooleanField()
    dau_xa_cfg_1_cr2_err_inj_mask_2  = models.BooleanField()
    dau_xa_cfg_1_cr2_err_inj_mask_3  = models.BooleanField()
    dau_xa_cfg_1_cr2_err_inj_mask_4  = models.BooleanField()
    dau_xa_cfg_1_cr2_err_inj_mask_5  = models.BooleanField()
    dau_xa_cfg_1_cr2_err_inj_mask_6  = models.BooleanField()
    dau_xa_cfg_1_cr2_err_inj_mask_7  = models.BooleanField()
    dau_xa_cfg_1_cr2_err_inj_mask_8  = models.BooleanField()
    dau_xa_cfg_1_sr0_now_scrub       = models.BooleanField()
    dau_xa_cfg_1_sr0_rfail           = models.BooleanField()
    dau_xa_cfg_1_sr0_rpass           = models.BooleanField()
    dau_xa_cfg_2_cr0_start_readback  = models.BooleanField()
    dau_xa_cfg_2_cr0_reset_status    = models.BooleanField()
    dau_xa_cfg_2_cr0_start_config    = models.BooleanField()
    dau_xa_cfg_2_cr1_serial_clock_div= models.IntegerField()
    dau_xa_cfg_2_cr2_err_inj_mask_1  = models.BooleanField()
    dau_xa_cfg_2_cr2_err_inj_mask_2  = models.BooleanField()
    dau_xa_cfg_2_cr2_err_inj_mask_3  = models.BooleanField()
    dau_xa_cfg_2_cr2_err_inj_mask_4  = models.BooleanField()
    dau_xa_cfg_2_cr2_err_inj_mask_5  = models.BooleanField()
    dau_xa_cfg_2_cr2_err_inj_mask_6  = models.BooleanField()
    dau_xa_cfg_2_cr2_err_inj_mask_7  = models.BooleanField()
    dau_xa_cfg_2_cr2_err_inj_mask_8  = models.BooleanField()
    dau_xa_cfg_2_sr0_now_scrub       = models.BooleanField()
    dau_xa_cfg_2_sr0_rfail           = models.BooleanField()
    dau_xa_cfg_2_sr0_rpass           = models.BooleanField()
    dau_xa_cfg_3_cr0_start_readback  = models.BooleanField()
    dau_xa_cfg_3_cr0_reset_status    = models.BooleanField()
    dau_xa_cfg_3_cr0_start_config    = models.BooleanField()
    dau_xa_cfg_3_cr1_serial_clock_div= models.IntegerField()
    dau_xa_cfg_3_cr2_err_inj_mask_1  = models.BooleanField()
    dau_xa_cfg_3_cr2_err_inj_mask_2  = models.BooleanField()
    dau_xa_cfg_3_cr2_err_inj_mask_3  = models.BooleanField()
    dau_xa_cfg_3_cr2_err_inj_mask_4  = models.BooleanField()
    dau_xa_cfg_3_cr2_err_inj_mask_5  = models.BooleanField()
    dau_xa_cfg_3_cr2_err_inj_mask_6  = models.BooleanField()
    dau_xa_cfg_3_cr2_err_inj_mask_7  = models.BooleanField()
    dau_xa_cfg_3_cr2_err_inj_mask_8  = models.BooleanField()
    dau_xa_cfg_3_sr0_now_scrub       = models.BooleanField()
    dau_xa_cfg_3_sr0_rfail           = models.BooleanField()
    dau_xa_cfg_3_sr0_rpass           = models.BooleanField()
    dau_xa_cfg_4_cr0_start_readback  = models.BooleanField()
    dau_xa_cfg_4_cr0_reset_status    = models.BooleanField()
    dau_xa_cfg_4_cr0_start_config    = models.BooleanField()
    dau_xa_cfg_4_cr1_serial_clock_div= models.IntegerField()
    dau_xa_cfg_4_cr2_err_inj_mask_1  = models.BooleanField()
    dau_xa_cfg_4_cr2_err_inj_mask_2  = models.BooleanField()
    dau_xa_cfg_4_cr2_err_inj_mask_3  = models.BooleanField()
    dau_xa_cfg_4_cr2_err_inj_mask_4  = models.BooleanField()
    dau_xa_cfg_4_cr2_err_inj_mask_5  = models.BooleanField()
    dau_xa_cfg_4_cr2_err_inj_mask_6  = models.BooleanField()
    dau_xa_cfg_4_cr2_err_inj_mask_7  = models.BooleanField()
    dau_xa_cfg_4_cr2_err_inj_mask_8  = models.BooleanField()
    dau_xa_cfg_4_sr0_now_scrub       = models.BooleanField()
    dau_xa_cfg_4_sr0_rfail           = models.BooleanField()
    dau_xa_cfg_4_sr0_rpass           = models.BooleanField()
    dau_dm_if_1_cr0_snap             = models.BooleanField()
    dau_dm_if_1_cr1_timeout          = models.IntegerField()
    dau_dm_if_1_cr1_snapen           = models.BooleanField()
    dau_dm_if_1_cr1_offs_baseline_corr = models.BooleanField()
    dau_dm_if_1_cr1_hit_artificial_trigs = models.BooleanField()
    dau_dm_if_1_cr1_disable_module = models.BooleanField()
    dau_dm_if_1_cr2_decf_data_reduc_factor = models.IntegerField()
    dau_dm_if_1_cr3_adc_delayed_sample_time= models.IntegerField()
    dau_dm_if_1_cr3_adrtime_pixel_address = models.IntegerField()
    dau_dm_if_1_sr0_depends_snapen = models.IntegerField()
    dau_dm_if_1_sr1_depends_snapen_0 = models.IntegerField()
    dau_dm_if_1_sr1_depends_snapen_1 = models.IntegerField()
    dau_dm_if_1_sr2_depends_snapen = models.IntegerField()
    dau_dm_if_1_sr3_depends_snapen = models.IntegerField()

    dau_dm_if_2_cr0_snapshot_address_en = models.IntegerField()
    dau_dm_if_2_cr1_timeout          = models.IntegerField()
    dau_dm_if_2_cr1_snapen           = models.BooleanField()
    dau_dm_if_2_cr1_offs_baseline_corr = models.BooleanField()
    dau_dm_if_2_cr1_hit_artificial_trigs = models.BooleanField()
    dau_dm_if_2_cr1_disable_module = models.BooleanField()
    dau_dm_if_2_cr2_decf_data_reduc_factor = models.IntegerField()
    dau_dm_if_2_cr3_adc_delayed_sample_time= models.IntegerField()
    dau_dm_if_2_cr3_adrtime_pixel_address = models.IntegerField()
    dau_dm_if_2_sr0_depends_snapen = models.IntegerField()
    dau_dm_if_2_sr1_depends_snapen_0 = models.IntegerField()
    dau_dm_if_2_sr1_depends_snapen_1 = models.IntegerField()
    dau_dm_if_2_sr2_depends_snapen = models.IntegerField()
    dau_dm_if_2_sr3_depends_snapen = models.IntegerField()

    dau_dm_if_3_cr0_snapshot_address_en = models.IntegerField()
    dau_dm_if_3_cr1_timeout          = models.IntegerField()
    dau_dm_if_3_cr1_snapen           = models.BooleanField()
    dau_dm_if_3_cr1_offs_baseline_corr = models.BooleanField()
    dau_dm_if_3_cr1_hit_artificial_trigs = models.BooleanField()
    dau_dm_if_3_cr1_disable_module = models.BooleanField()
    dau_dm_if_3_cr2_decf_data_reduc_factor = models.IntegerField()
    dau_dm_if_3_cr3_adc_delayed_sample_time= models.IntegerField()
    dau_dm_if_3_cr3_adrtime_pixel_address = models.IntegerField()
    dau_dm_if_3_sr0_depends_snapen = models.IntegerField()
    dau_dm_if_3_sr1_depends_snapen_0 = models.IntegerField()
    dau_dm_if_3_sr1_depends_snapen_1 = models.IntegerField()
    dau_dm_if_3_sr2_depends_snapen = models.IntegerField()
    dau_dm_if_3_sr3_depends_snapen = models.IntegerField()

    dau_dm_if_4_cr0_snapshot_address_en = models.IntegerField()
    dau_dm_if_4_cr1_timeout          = models.IntegerField()
    dau_dm_if_4_cr1_snapen           = models.BooleanField()
    dau_dm_if_4_cr1_offs_baseline_corr = models.BooleanField()
    dau_dm_if_4_cr1_hit_artificial_trigs = models.BooleanField()
    dau_dm_if_4_cr1_disable_module = models.BooleanField()
    dau_dm_if_4_cr2_decf_data_reduc_factor = models.IntegerField()
    dau_dm_if_4_cr3_adc_delayed_sample_time= models.IntegerField()
    dau_dm_if_4_cr3_adrtime_pixel_address = models.IntegerField()
    dau_dm_if_4_sr0_depends_snapen = models.IntegerField()
    dau_dm_if_4_sr1_depends_snapen_0 = models.IntegerField()
    dau_dm_if_4_sr1_depends_snapen_1 = models.IntegerField()
    dau_dm_if_4_sr2_depends_snapen = models.IntegerField()
    dau_dm_if_4_sr3_depends_snapen = models.IntegerField()
    
    dau_rcu_master_cr0_startscrub = models.BooleanField()
    dau_rcu_master_cr0_edacerst = models.BooleanField()
    dau_rcu_master_cr0_sdctest = models.BooleanField()
    dau_rcu_master_cr0_mrst_master_reset = models.BooleanField()

    dau_rcu_master_cr1_scrubstop = models.BooleanField()
    dau_rcu_master_cr1_asic_set_version = models.BooleanField()
    dau_rcu_master_cr1_test_mode_enable = models.BooleanField()

    dau_rcu_master_cr2_mtest_multihit = models.BooleanField()
    dau_rcu_master_cr2_ttest_timetag = models.BooleanField()
    dau_rcu_master_cr2_atest_address_test = models.BooleanField()
    dau_rcu_master_cr2_etest_energy_test = models.BooleanField()

    dau_rcu_master_cr3_noblink_inhibit_led = models.BooleanField()
    dau_rcu_master_cr3_debugsel = models.IntegerField()

    dau_rcu_master_sr0_firmware_version_low_byte = models.IntegerField()
    dau_rcu_master_sr1_firmware_version_high_byte = models.IntegerField()
    dau_rcu_master_sr2_err_uncorrectable_double = models.IntegerField()
    dau_rcu_master_sr3_corr_correctable_single = models.IntegerField()

    dau_bcm_cr1_mhfilt_4_or_more  = models.BooleanField()
    dau_bcm_cr1_mhfilt_3_simultaneous  = models.BooleanField()
    dau_bcm_cr1_mhfilt_2_simultaneous  = models.BooleanField()
    dau_bcm_cr1_mhfilt_1_simultaneous  = models.BooleanField()
    dau_bcm_sr0_hitcntl_total_hit_low = models.IntegerField()
    dau_bcm_sr1_hitcntl_total_hit_middle = models.IntegerField()
    dau_bcm_sr2_hitcntl_total_hit_high = models.IntegerField()
    dau_bcm_cr_spectral_boundary_low = models.IntegerField()
    dau_bcm_cr_spectral_boundary_1 = models.IntegerField()
    dau_bcm_cr_spectral_boundary_2 = models.IntegerField()
    dau_bcm_cr_spectral_boundary_3 = models.IntegerField()
    dau_bcm_cr_spectral_boundary_4 = models.IntegerField()
    dau_bcm_cr_spectral_boundary_5 = models.IntegerField()
    dau_bcm_cr_spectral_boundary_6 = models.IntegerField()
    dau_bcm_cr_spectral_boundary_7 = models.IntegerField()
    dau_bcm_cr_spectral_boundary_8 = models.IntegerField()
    dau_bcm_cr_spectral_boundary_9 = models.IntegerField()
    dau_bcm_cr_spectral_boundary_high = models.IntegerField()
    dau_bcm_cr_temporal_bin_size = models.IntegerField()
    spare_sr0_multi_hit_counter_low_byte = models.IntegerField()
    spare_sr1_multi_hit_counter_middle_byte = models.IntegerField()
    spare_sr2_multi_hit_counter_high_byte = models.IntegerField()

