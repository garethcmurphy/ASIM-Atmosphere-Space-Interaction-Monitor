
import requests
from bs4 import BeautifulSoup

import math
import time
from datetime import datetime, timedelta
import ephem
import numpy as np
 



def scrapetle():
    url = 'http://celestrak.com/NORAD/elements/stations.txt'
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, "lxml")
    mytle=(soup.text[:168])
    lines = mytle.splitlines()
    return (lines)


def getantimeridancrossingtime(time):

    #mydate=datetime(2016, 4, 7, 9, 10, 45)

    home.date=mydatenow
    iss.compute(home)

    issorbitsperday=15.54459501994820
    issorbitalperiod=24*60/issorbitsperday


    print ("ISS sublong" , iss.sublong)
    sublong=iss.sublong.real

    print ("Position in degrees", sublong*180/np.pi)

    radtodeg=180/np.pi

    angletoam=(sublong+np.pi)
    angletoamdeg=angletoam*radtodeg
    print ("Angle to AM in degrees", angletoam*radtodeg)
    timetoam=(angletoamdeg)*issorbitalperiod/360


    deltatoam=timedelta(minutes=timetoam)
    mydate=mydatenow-deltatoam


    print ("Minutes to antimeridian" , timetoam)

    print ("time Delta to antimeridian" , deltatoam)
    print ("Now ", mydatenow)

    print ("Antimeridian time", mydate)
    home.date = mydate
    iss.compute(home)
            
    print (iss.sublong)
    return (mydate)


def getorbit(mydate,npoints):
    lonarr=[0] * npoints
    latarr=[0] * npoints
#for q in range (0,2):
    for i in range(0,npoints):
        one_hour = timedelta(hours=1)
        min15 = timedelta(minutes=5)
        #mydate=datearr[q]
        #mydate=datetime(a[0], a[1], a[2], a[3], a[4], a[5])
        home.date = mydate +i*min15
        iss.compute(home)
        dist=2
        lonarr[i]=iss.sublong* degrees_per_radian
        latarr[i]=iss.sublat* degrees_per_radian
        #if ( (iss.alt < dist) and (iss.az < dist)):
        #    print (home.date)
        #    print('iss: altitude %4.1f deg, azimuth %5.1f deg' % (iss.alt * degrees_per_radian, iss.az * degrees_per_radian))
 
    print (lonarr)
    print (latarr)
    return (lonarr, latarr)
