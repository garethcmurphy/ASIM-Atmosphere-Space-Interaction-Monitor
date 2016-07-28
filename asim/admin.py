from django.contrib import admin


# Register your models here.


from asim.models import *

admin.site.register(ScienceData)
admin.site.register(BackgroundObservation)
#admin.site.register(ISSpredict)
admin.site.register(MXGSAuroralCaptureObservation)
admin.site.register(MXGSBGODAU1FullHousekeepingTM)
admin.site.register(MXGSBGODAU2FullHousekeepingTM)
admin.site.register(MXGSBGODAU3FullHousekeepingTM)
admin.site.register(MXGSBGODAU4FullHousekeepingTM)
admin.site.register(MXGSBGODAUFullHousekeepingTM)
admin.site.register(MXGSBGODAUSummaryHousekeepingTM)
admin.site.register(MXGSBufferResourceHousekeeping)
#admin.site.register(MXGSCZTDAU1FullHousekeepingTM)
#admin.site.register(MXGSCZTDAU2FullHousekeepingTM)
#admin.site.register(MXGSCZTDAU3FullHousekeepingTM)
#admin.site.register(MXGSCZTDAU4FullHousekeepingTM)
admin.site.register(MXGSCZTDAUFullHousekeepingTM)
admin.site.register(MXGSCZTDAUHousekeepingTM)
admin.site.register(MXGSCZTDAUSummaryHousekeepingTM)
admin.site.register(MXGSDPUHousekeepingTM)
admin.site.register(MXGSEnableInstrumentEvent)
admin.site.register(MXGSEventReport)
admin.site.register(MXGSHousekeepingTC)
admin.site.register(MXGSInstrumentHousekeepingTM)
admin.site.register(MXGSInstrumentSummaryHousekeepingTM)
admin.site.register(MXGSMonitoredHousekeepingTM)
admin.site.register(MXGSPSUFullHousekeepingTM)
admin.site.register(MXGSPulseHeightSpectrumObservation)
admin.site.register(MXGSRatemeterHousekeeping)
admin.site.register(MXGSSampledDetectorCounts)
admin.site.register(MXGSStartupHousekeepingTM)
admin.site.register(MXGSTGFObservation)
admin.site.register(OrbitModel)

