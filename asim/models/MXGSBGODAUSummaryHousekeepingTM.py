from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin


class MXGSBGODAUSummaryHousekeepingTM(models.Model):
    utc_year                        = models.IntegerField('UTC year')
    

