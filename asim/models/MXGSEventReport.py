from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin

class MXGSEventReport (models.Model):
    packet_length                   = models.IntegerField('Packet length')
    INFORMATION = "INF"
    ADVISORY = "ADV"
    CAUTION = "CAU"
    WARNING = "WAR"
    EMERGENCY = "EME"
    EVENT_SEVERITY_CHOICES = (
        (INFORMATION, "Information"),
        (ADVISORY, "Advisory"),
        (CAUTION, "Caution"),
        (WARNING, "Warning"),
        (EMERGENCY, "Emergency")
    )
    event_severity = models.CharField(max_length=3,
                                         choices=EVENT_SEVERITY_CHOICES,
                                         default=INFORMATION)
    EVENT_30000 = "30000"
    EVENT_30010 = "30010"
    EVENT_30090 = "30090"
    EVENT_30100 = "30100"
    EVENT_30110 = "30110"
    EVENT_30120 = "30120"
    EVENT_30130 = "30130"
    EVENT_30140 = "30140"
    EVENT_30160 = "30160"
    EVENT_40000 = "40000"
    EVENT_40010 = "40010"
    EVENT_40020 = "40020"
    EVENT_40030 = "40030"
    EVENT_40040 = "40040"
    EVENT_40050 = "40050"
    EVENT_40090 = "40090"
    EVENT_40100 = "40100"
    EVENT_40110 = "40110"
    EVENT_40120 = "40120"
    EVENT_40150 = "40150"
    EVENT_40160 = "40160"
    EVENT_40170 = "40170"
    EVENT_40180 = "40180"
    EVENT_40190 = "40190"
    EVENT_40200 = "40200"
    EVENT_40210 = "40210"
    EVENT_40260 = "40260"
    EVENT_40270 = "40270"
    EVENT_40280 = "40280"
    EVENT_40290 = "40290"

    EVENT_ID_CHOICES = (
        (EVENT_30000, "Software change, severity 0"),
        (EVENT_30010, "Submode change, severity 0"),
        (EVENT_30090, "Science observation with priority 3 discarded due to data collection buffer being full, severity 1"),
        (EVENT_30100, "Science observation with priority 2 discarded due to data collection buffer being full, severity 2"),
        (EVENT_30110, "Science observation with priority 1 discarded due to data collection buffer being full, severity 3"),
        (EVENT_30120, "Science observation transferred from data collection buffer to science downlink buffer, severity 0"),
        (EVENT_30130, "Science downlink buffer full, data transfer function is suspended, severity 1"),
        (EVENT_30140, "Science downlink buffer has free space after being full, data transfer function is resumed, severity 0"),
        (EVENT_30160, "Trigger occurred in TGF search window, trigger is sent to MMIA, severity 0"),
        (EVENT_40000, "Validation of parameters of a configuration table failed, severity 3"),
        (EVENT_40010, "LHP Startup heaters powered on, severity 0"),
        (EVENT_40020, "LHP Startup heaters powered off, severity 0"),
        (EVENT_40030, "Front-End Ring Buffer FIFO, implemented in the DPU FPGA for incoming Detector Event Data, becomes full, severity 3"),
        (EVENT_40040, "Front-End Ring Buffer FIFO, implemented in the DPU FPGA for incoming Detector Event Data, has free space available again immediately after being full, severity 2"),
        (EVENT_40050, "trigger occurs in one or more TGF search windows, or when a trigger is received from MMIA, severity 0"),
        (EVENT_40090, "successful transfer of a TGF Observation to the Data Collection Buffer, severity 1"),
        (EVENT_40100, "ratemeter readings of LED Accepted Counts and HED Accepted Counts are available for background rate calculations and adjustment of trigger thresholds, severity 0"),
        (EVENT_40110, "successful transfer of a Background Data Observation to the Data Collection Bufferi, severity 0"),
        (EVENT_40120, "successful transfer of a Sampled Detector Events Observation to the Data Collection Bufferi, severity 0"),
        (EVENT_40150, "successful transfer of a  Pulse-Height Spectrum to the Data Collection Bufferi, severity 0"),
        (EVENT_40160, "background rate estimate for the next 1-second period has been successfully calculated for both detector planes, severity 0"),
        (EVENT_40170, "one or more of the TGF Trigger Thresholds is changed. Note that it is not transmitted at 1-second intervals, but only when there is a change in one or more thresholds, severity 1"),
        (EVENT_40180, "Data Reduction Factor (Q) commanded to the DAUs is changed, severity 1"),
        (EVENT_40190, "DPU starts to acquire high-time-resolution histograms directly from the DAUs in Auroral Capture Submode, severity 0"),
        (EVENT_40200, "DPU ends acquisition of high-time-resolution histograms in Auroral Capture Submode, severity 0"),
        (EVENT_40210, "successful transfer of an Auroral Capture Observation to the Data Collection Buffer, severity 0"),
        (EVENT_40260, "loading configuration data to the DAU and/or PSU has failed, severity 3"),
        (EVENT_40270, " loading configuration data to the DAU and/or PSU has been successful, severity 0"),
        (EVENT_40280, " accepted counts ratemeter acquired directly from the DAU is too high and would result in an algorithm overflow, severity 3"),
        (EVENT_40290, "one or more software task scheduling errors are detected, severity 3"),

    )
    event_id = models.CharField(max_length=5,
                                choices=EVENT_SEVERITY_CHOICES,
                                default=EVENT_30000)


    
    event_id                        = models.IntegerField()
    utc_year                        = models.IntegerField('UTC year')
    utc_msec                        = models.IntegerField('UTC msec')
    utc_seconds                     = models.IntegerField('UTC seconds')

