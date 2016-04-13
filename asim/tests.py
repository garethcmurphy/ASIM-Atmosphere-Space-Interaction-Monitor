import datetime
from django.utils import timezone
from django.test import TestCase

# Create your tests here.
from asim.models import ScienceData

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



