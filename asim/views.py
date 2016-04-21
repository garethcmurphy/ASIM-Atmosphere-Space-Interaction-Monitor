from django.shortcuts import get_object_or_404, render, render_to_response
from django.core.urlresolvers import reverse
from asim.utils import scrapetle


# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse

from django.template import loader
from datetime import datetime, timedelta

from .models import ScienceData
from .models import ISSpredict
from .forms import NameForm
from asim.forms import LocForm

import ephem
import numpy as np

def index(request):
    latest_sciencedata_list = ScienceData.objects.order_by('-date')[:5]
    context = { 'latest_sciencedata_list': latest_sciencedata_list }
    return  render(request, 'asim/index.html', context)
    


def browse(request):
    latest_sciencedata_list = ScienceData.objects.order_by('-date')[:10]
    context = { 'latest_sciencedata_list': latest_sciencedata_list }
    return  render(request, 'asim/browse.html', context)
    

def orbitdisplay(request):
    home = ephem.Observer()
    home.lon = '0'   # +E
    home.lat = '0'      # +N
    home.elevation = 50 # meters
# Always get the latest ISS TLE data from:
# http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html
    iss = ephem.readtle('ISS',
        '1 25544U 98067A   16103.90629446  .00006076  00000-0  97790-4 0  9996',
        '2 25544  51.6437  23.6320 0002668  61.0097  30.5624 15.54459501994820'
    )
    mydatenow=datetime.utcnow()
    home.date=mydatenow
    iss.compute(home)
    latest_sciencedata_list = ScienceData.objects.order_by('-date')[:10]
    radtodeg=180./np.pi
    lon=iss.sublong.real*radtodeg
    lat=iss.sublat.real*radtodeg
    context = { 'latest_sciencedata_list': latest_sciencedata_list, 'lat' : lat, 'lon' : lon, }
    current_name='Paris'
    return  render(request, 'asim/orbitdisplay.html', context)
    
def your_location(request):
   latest_sciencedata_list = ScienceData.objects.order_by('-date')[:10]
   context = { 'latest_sciencedata_list': latest_sciencedata_list }
   return render(request, 'asim/your_location.html', {'results': results})


def location(request):
    if request.method == "POST":
        form = LocForm(request.POST)
        print ( "form is valid or not", form.is_valid())
        if form.is_valid():
            placename   = form.cleaned_data['placename']
            lat         = form.cleaned_data['lat']
            lon         = form.cleaned_data['lon']
            e=ISSpredict(id=1)
            e.userselect=0
            e.lat=float(lat)
            e.lon=float(lon)
            e.save()
            #print ("lat ",lat)
            return HttpResponseRedirect(reverse('asim:thanks', ))
    else:
        form = LocForm()

    return render(request, 'asim/location.html', {'form': form})

def thanks(request):
    e=ISSpredict.objects.get(id=1)
    lat=e.lat
    lon=e.lon
    print (lat, lon)
    context = {  'lat' : lat, 'lon' : lon, }
    return render(request, 'asim/orbitdisplay.html', context)

def detail(request, obsid):
    sciencedata = get_object_or_404(ScienceData, obsid=obsid)
    objects= ScienceData.objects.all()

    for object in objects:
        object.fields = dict((field.name, field.value_to_string(object))
                                            for field in object._meta.fields)
    return render(request, 'asim/detail.html', {'sciencedata': sciencedata})
#    return render(request, 'asim/detail.html', {'objects': objects})
#    return render_to_response(template, { 'objects':objects }, context_instance=RequestContext(request))

def results(request, obsid):
    response = "You're looking at result of obsid %s."
    return HttpResponse(response % obsid)

def vote(request, obsid):
    return HttpResponse("You're modifying  obs id  %s." % obsid)



def search(request):
    results = None
    query = request.GET.get('q')
    try:
        query = (query)
    except ValueError:
        query = None
        results = None
    if query:
        results = ScienceData.objects.filter(obsid=query)
    #context = RequestContext(request)
    return render(request, 'asim/results.html', {'results': results})


 

def get_name(request):
    obsidres=0
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            searchterm=form.save(commit=False)
            obsidres= ScienceData.objects.filter(obsid=request_params['form'])
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'asim/search_results.html', {'results': obsidres})



