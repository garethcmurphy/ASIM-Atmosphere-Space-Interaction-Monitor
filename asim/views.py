from django.shortcuts import get_object_or_404, render, render_to_response

# Create your views here.
from django.http import HttpResponse

from django.template import loader

from .models import ScienceData
from .forms import NameForm


def index(request):
    latest_sciencedata_list = ScienceData.objects.order_by('-date')[:5]
    context = { 'latest_sciencedata_list': latest_sciencedata_list }
    return  render(request, 'asim/index.html', context)
    


def browse(request):
    latest_sciencedata_list = ScienceData.objects.order_by('-date')[:10]
    context = { 'latest_sciencedata_list': latest_sciencedata_list }
    return  render(request, 'asim/browse.html', context)
    


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



