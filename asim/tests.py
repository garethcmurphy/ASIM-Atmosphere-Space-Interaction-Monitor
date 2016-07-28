import datetime
from django.utils import timezone
from django.test import TestCase

# Create your tests here.
from asim.models import *


class MyTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.mxgsstartuphousekeepingtm=MXGSStartupHousekeepingTM.objects.create(
         tcp_count_dpu                   = 1,
            acquisition_start_time_current  = 1,
            boot_status_completed_with_errors = 0,
            boot_status_completed_no_errors = 0,
            boot_status_asw_load_ok         = 0,
            boot_status_system_memory_test_ok = 0,
            boot_software_version_major     = 1,
            boot_software_version_minor     = 1,
            app_software_version_major      = 1,
            app_software_version_minor      = 1,
            app_software_version_patch      = 1
        )
        mytgfobs=MXGSTGFObservation(
            observation_id                  =7001,
            utc_year                        =2016,
            utc_seconds                     =117,
            utc_msec                        =1100,
            tcp_count_dhpu                  =8, 
            tcp_count_dpu                   =8, 
            dpu_count                       =8, 
            dpu_count_prereset              =8, 
            dau_bgo_1_int_tmon_chan1        =8, 
            dau_bgo_1_int_tmon_chan2        =8, 
            dau_bgo_1_int_tmon_chan3        =8, 
            dau_bgo_1_int_tmon_chan4        =8, 
            dau_bgo_2_int_tmon_chan1        =8, 
            dau_bgo_2_int_tmon_chan2        =8, 
            dau_bgo_2_int_tmon_chan3        =8, 
            dau_bgo_2_int_tmon_chan4        =8, 
            dau_bgo_3_int_tmon_chan1        =8, 
            dau_bgo_3_int_tmon_chan2        =8, 
            dau_bgo_3_int_tmon_chan3        =8, 
            dau_bgo_3_int_tmon_chan4        =8, 
            dau_bgo_4_int_tmon_chan1        =8, 
            dau_bgo_4_int_tmon_chan2        =8, 
            dau_bgo_4_int_tmon_chan3        =8, 
            dau_bgo_4_int_tmon_chan4        =8, 
            led_short_win_lr_pulse_height   =8, 
            led_short_win_upr_pulse_height  =8, 
            led_long_win_lr_pulse_height    =8, 
            led_long_win_upr_pulse_height   =8, 
            hed_short_win_lr_pulse_height   =8, 
            hed_short_win_upr_pulse_height  =8, 
            hed_long_win_lr_pulse_height    =8, 
            hed_long_win_upr_pulse_height   =8, 
            led_short_win_anticoin_time     =8, 
            led_long_win_anticoin_time      =8, 
            hed_short_win_anticoin_time     =8, 
            hed_long_win_anticoin_time      =8, 
            led_short_win_flag1             =1,
            led_short_win_flag2             =1,
            led_short_win_flag3             =1,
            led_long_win_flag               =1,
            hed_short_win_flag1             =1,
            hed_short_win_flag2             =1,
            hed_short_win_flag3             =1,
            hed_long_win_flag               =1,
            trig_mmia_enabled               =1,
            trig_mmia_recd                  =1,
            led_short_win_dur_1             =8, 
            led_short_win_dur_2             =8, 
            led_short_win_dur_3             =8, 
            led_long_win_dur                =8, 
            hed_short_win_dur_1             =8, 
            hed_short_win_dur_2             =8, 
            hed_short_win_dur_3             =8, 
            hed_long_win_dur                =8, 
            led_short_win_thresh_1          =8, 
            led_short_win_thresh_2          =8, 
            led_short_win_thresh_3          =8, 
            led_long_win_thresh             =8, 
            hed_short_win_thresh_1          =8, 
            hed_short_win_thresh_2          =8, 
            hed_short_win_thresh_3          =8, 
            hed_long_win_thresh             =8, 
            mxgs_trig_count                 =200,
            mxgs_trig_tcp_count             =8, 
            mxgs_trig_dpu_count             =8, 
            num_counts                      =8, 
            detector_counts                 ='asimdata/2016/117/mydata.cdf'  
         )
        #q.save()

class ScienceDataTestCase(TestCase):
    def setUp(self):
        ScienceData.objects.create( lat=57.3, lon=12.1, obsid=7778, trig='bluejet' , date=timezone.now() ,  lev0='lev0.cdf', lev1='lev1.cdf' , prev='prev.png')

    def test_was_published_recently_with_future_sciencedata(self):
        """
        was_published_recently() should return False for ScienceData whose
        date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = ScienceData(date=time)
        self.assertEqual(future_question.was_published_recently(), False)



