from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin


# Create your models here.


    


class ScienceData(models.Model):
    lat=models.FloatField('Latitude')
    lon=models.FloatField('Longitude')
    obsid=models.IntegerField('ObservationId')
    date=models.DateTimeField('Date Observed')
    trig=models.CharField(max_length=200)
    inst=models.CharField(max_length=200)
    lev0=models.CharField(max_length=200)
    lev1=models.CharField(max_length=200)
    prev=models.CharField(max_length=200)
    def __str__(self):
        return 'Lat: '+str(float(self.lat))+' , Lon: '+str(float(self.lon))+' , ObsId: '+str(int(self.obsid))
 
    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)

