from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin

def hex2int(charstr):
    return int(charstr,16)

class MXGSTGFObservation(models.Model):
    observation_id                  =models.IntegerField('Observation ID')
    utc_year                        =models.IntegerField('UTC year')
    utc_seconds                     =models.IntegerField('UTC seconds')
    utc_msec                        =models.IntegerField('UTC msec')
    tcp_count_dhpu                  =models.IntegerField()
    tcp_count_dpu                   =models.IntegerField()
    dpu_count                       =models.IntegerField()
    dpu_count_prereset              =models.IntegerField()
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
    led_short_win_flag1             =models.BooleanField()
    led_short_win_flag2             =models.BooleanField()
    led_short_win_flag3             =models.BooleanField()
    led_long_win_flag               =models.BooleanField()
    hed_short_win_flag1             =models.BooleanField()
    hed_short_win_flag2             =models.BooleanField()
    hed_short_win_flag3             =models.BooleanField()
    hed_long_win_flag               =models.BooleanField()
    trig_mmia_enabled               =models.BooleanField()
    trig_mmia_recd                  =models.BooleanField()
    led_short_win_dur_1             =models.IntegerField()
    led_short_win_dur_2             =models.IntegerField()
    led_short_win_dur_3             =models.IntegerField()
    led_long_win_dur                =models.IntegerField()
    hed_short_win_dur_1             =models.IntegerField()
    hed_short_win_dur_2             =models.IntegerField()
    hed_short_win_dur_3             =models.IntegerField()
    hed_long_win_dur                =models.IntegerField()
    led_short_win_thresh_1          =models.IntegerField()
    led_short_win_thresh_2          =models.IntegerField()
    led_short_win_thresh_3          =models.IntegerField()
    led_long_win_thresh             =models.IntegerField()
    hed_short_win_thresh_1          =models.IntegerField()
    hed_short_win_thresh_2          =models.IntegerField()
    hed_short_win_thresh_3          =models.IntegerField()
    hed_long_win_thresh             =models.IntegerField()
    mxgs_trig_count                 =models.BigIntegerField()
    mxgs_trig_tcp_count             =models.IntegerField()
    mxgs_trig_dpu_count             =models.IntegerField()
    num_counts                      =models.IntegerField()
    detector_counts                 =models.FileField()
    
    def hexstring_to_db (self, masterdata):
        x=iter(masterdata)
        
        header=x.next()+x.next()


        self.packet_length                   = hex2int (x.next())
        self.observation_id                  = hex2int (x.next())
        continuation_id                 = hex2int (x.next())
        last_packet                     = hex2int (x.next())
        self.utc_year                        = hex2int(x.next())
        self.utc_msec                        = hex2int(x.next())
        self.utc_seconds                     = hex2int (x.next()+x.next())
        self.tcp_count_dhpu                  = hex2int (x.next()+x.next())
        self.tcp_count_dpu                   = hex2int (x.next()+x.next())
        self.dpu_count                       = hex2int (x.next()+x.next())
        self.dpu_count_prereset              = hex2int (x.next()+x.next())
        self.dau_bgo_1_int_tmon_chan1        = hex2int (x.next())
        self.dau_bgo_1_int_tmon_chan2        = hex2int (x.next())
        self.dau_bgo_1_int_tmon_chan3        = hex2int (x.next())
        self.dau_bgo_1_int_tmon_chan4        = hex2int (x.next())
        self.dau_bgo_2_int_tmon_chan1        = hex2int (x.next())
        self.dau_bgo_2_int_tmon_chan2        = hex2int (x.next())
        self.dau_bgo_2_int_tmon_chan3        = hex2int (x.next())
        self.dau_bgo_2_int_tmon_chan4        = hex2int (x.next())
        self.dau_bgo_3_int_tmon_chan1        = hex2int (x.next())
        self.dau_bgo_3_int_tmon_chan2        = hex2int (x.next())
        self.dau_bgo_3_int_tmon_chan3        = hex2int (x.next())
        self.dau_bgo_3_int_tmon_chan4        = hex2int (x.next())
        self.dau_bgo_4_int_tmon_chan1        = hex2int (x.next())
        self.dau_bgo_4_int_tmon_chan2        = hex2int (x.next())
        self.dau_bgo_4_int_tmon_chan3        = hex2int (x.next())
        self.dau_bgo_4_int_tmon_chan4        = hex2int (x.next())
        self.led_short_win_lr_pulse_height  = hex2int (x.next()) 
        self.led_short_win_upr_pulse_height = hex2int (x.next()) 
        self.led_long_win_lr_pulse_height   = hex2int (x.next()) 
        self.led_long_win_upr_pulse_height  = hex2int (x.next()) 
        self.hed_short_win_lr_pulse_height  = hex2int (x.next()) 
        self.hed_short_win_upr_pulse_height = hex2int (x.next()) 
        self.hed_long_win_lr_pulse_height   = hex2int (x.next()) 
        self.hed_long_win_upr_pulse_height  = hex2int (x.next()) 


        shortlongwin=x.next()
        self.led_short_win_anticoin_time = hex2int (shortlongwin[0:2]) 
        self.led_long_win_anticoin_time  = hex2int (shortlongwin[2:4]) 
        shortlongwin=x.next()
        self.hed_short_win_anticoin_time = hex2int (shortlongwin[0:2]) 
        self.hed_long_win_anticoin_time  = hex2int (shortlongwin[2:4])

        bits=x.next()

        from bitstring import BitArray

        a = BitArray('0x'+bits)
        self.led_short_win_flag1 = a[0]
        self.led_short_win_flag2 = a[1]
        self.led_short_win_flag3 = a[2]
        self.led_long_win_flag   = a[3]
        self.hed_short_win_flag1 = a[4]
        self.hed_short_win_flag2 = a[5]
        self.hed_short_win_flag3 = a[6]
        self.hed_long_win_flag   = a[7]


        self.trig_mmia_enabled = a[8]
        self.trig_mmia_recd = a[9]


        self.led_short_win_dur_1 =  hex2int (x.next()) 
        self.led_short_win_dur_2 = hex2int (x.next()) 
        self.led_short_win_dur_3 = hex2int (x.next()) 
        self.led_long_win_dur    = hex2int (x.next()) 
        self.hed_short_win_dur_1 = hex2int (x.next()) 
        self.hed_short_win_dur_2 = hex2int (x.next()) 
        self.hed_short_win_dur_3 = hex2int (x.next()) 
        self.hed_long_win_dur    = hex2int (x.next()) 




        scrh=x.next()

        self.led_short_win_thresh_1 = hex2int (scrh[0:2])
        self.led_short_win_thresh_2 = hex2int (scrh[2:4]) 

        scrh1=x.next()
        scrh2=x.next()
        scrh3=x.next()

        self.led_short_win_thresh_3 = hex2int (scrh1[0:2]) 
        self.led_long_win_thresh    = hex2int (scrh1[2:4]+scrh2[0:2]) 
        self.hed_short_win_thresh_1 = hex2int (scrh2[2:4]) 
        self.hed_short_win_thresh_2 = hex2int (scrh3[0:2]) 
        self.hed_short_win_thresh_3 = hex2int (scrh3[2:4]) 
        self.hed_long_win_thresh    = hex2int (x.next()) 



        self.mxgs_trig_count = hex2int (x.next()+x.next()+x.next()+x.next() )
        self.mxgs_trig_tcp_count = hex2int (x.next()+x.next()) 
        self.mxgs_trig_dpu_count = hex2int (x.next()+x.next()) 
        self.num_counts = hex2int (x.next()+x.next())

        import itertools
        det_ev=list(itertools.islice(x,  None  ))   
        arr=[i+j+k+l for i,j,k,l in zip(det_ev[::4], det_ev[1::4] , det_ev[2::4], det_ev[3::4])]

        cdfname="./tgfobservation_"+header+str(self.observation_id).zfill(4)+".cdf"


        self.detector_counts = cdfname

        import spacepy
        from spacepy import pycdf
        import os
        try:
            os.remove(cdfname)
        except OSError:
            pass
        pycdf.lib.set_backward(False)
        cdf = pycdf.CDF(cdfname, '')
        cdf['detector_counts'] = arr
        bad_keys=['mybadkey', 'continuation_id', 'last_packet', '_state', 'id']
        for key in sorted(self.__dict__.iterkeys()):
            if key not in bad_keys:
                 #print key #, self.__dict__[key]
                 cdf.attrs[key]=self.__dict__[key]
        cdf.attrs['Author'] = 'Gareth Murphy <gmurphy@space.dtu.dk>'
        cdf.attrs['CreateDate'] = datetime.datetime.now()

        #print (cdf)
        #print (cdf.attrs)
        print "different"
            

