from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin


def hex2int(charstr):
    return int(charstr,16)
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

    def hexstring_to_db(self, masterdata):
        x=iter(masterdata)
        header=x.next()+x.next()


        packet_length                   = hex2int (x.next())
        self.observation_id                  =  (x.next())
        continuation_id                 = hex2int (x.next())
        last_packet                     = hex2int (x.next())
        self.utc_year                        = hex2int(x.next())
        self.utc_msec                        = hex2int(x.next())
        self.utc_seconds                     = hex2int (x.next()+x.next())
        self.tcp_count_dhpu                  = hex2int (x.next()+x.next())
        self.tcp_count_dpu                  = hex2int (x.next()+x.next())


        self.start_dau_bgo_1_int_tmon_chan1        = hex2int (x.next())
        self.start_dau_bgo_1_int_tmon_chan2        = hex2int (x.next())
        self.start_dau_bgo_1_int_tmon_chan3        = hex2int (x.next())
        self.start_dau_bgo_1_int_tmon_chan4        = hex2int (x.next())
        self.start_dau_bgo_2_int_tmon_chan1        = hex2int (x.next())
        self.start_dau_bgo_2_int_tmon_chan2        = hex2int (x.next())
        self.start_dau_bgo_2_int_tmon_chan3        = hex2int (x.next())
        self.start_dau_bgo_2_int_tmon_chan4        = hex2int (x.next())
        self.start_dau_bgo_3_int_tmon_chan1        = hex2int (x.next())
        self.start_dau_bgo_3_int_tmon_chan2        = hex2int (x.next())
        self.start_dau_bgo_3_int_tmon_chan3        = hex2int (x.next())
        self.start_dau_bgo_3_int_tmon_chan4        = hex2int (x.next())
        self.start_dau_bgo_4_int_tmon_chan1        = hex2int (x.next())
        self.start_dau_bgo_4_int_tmon_chan2        = hex2int (x.next())
        self.start_dau_bgo_4_int_tmon_chan3        = hex2int (x.next())
        self.start_dau_bgo_4_int_tmon_chan4        = hex2int (x.next())

        self.integration_period  = hex2int (x.next()) 
        self.data_provided = hex2int (x.next()) 


        if ( self.data_provided ):
            n=12
        else:
            n=4



        import itertools
            
        pulse_heights_hex=list(itertools.islice(x,  None  ))  
        det_ev=pulse_heights_hex

        pulse_heights_int=map(hex2int , pulse_heights_hex)


        arr=pulse_heights_int
        # print pulse_heights_int[0:1024]


        print (len(pulse_heights_int))



        dataendmark1        = det_ev[-18]
        dataendmark2        = det_ev[-17]


        self.end_dau_bgo_1_int_tmon_chan1        = hex2int(det_ev[-16])
        self.end_dau_bgo_1_int_tmon_chan2        = hex2int(det_ev[-15])
        self.end_dau_bgo_1_int_tmon_chan3        = hex2int(det_ev[-14])
        self.end_dau_bgo_1_int_tmon_chan4        = hex2int(det_ev[-13])
        self.end_dau_bgo_2_int_tmon_chan1        = hex2int(det_ev[-12])
        self.end_dau_bgo_2_int_tmon_chan2        = hex2int(det_ev[-11])
        self.end_dau_bgo_2_int_tmon_chan3        = hex2int(det_ev[-10])
        self.end_dau_bgo_2_int_tmon_chan4        = hex2int(det_ev[-9])
        self.end_dau_bgo_3_int_tmon_chan1        = hex2int(det_ev[-8])
        self.end_dau_bgo_3_int_tmon_chan2        = hex2int(det_ev[-7])
        self.end_dau_bgo_3_int_tmon_chan3        = hex2int(det_ev[-6])
        self.end_dau_bgo_3_int_tmon_chan4        = hex2int(det_ev[-5])
        self.end_dau_bgo_4_int_tmon_chan1        = hex2int(det_ev[-4])
        self.end_dau_bgo_4_int_tmon_chan2        = hex2int(det_ev[-3])
        self.end_dau_bgo_4_int_tmon_chan3        = hex2int(det_ev[-2])
        self.end_dau_bgo_4_int_tmon_chan4        = hex2int(det_ev[-1])


        cdfname="./pulseheightspectrum_"+header+str(self.observation_id).zfill(4)+".cdf"


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
