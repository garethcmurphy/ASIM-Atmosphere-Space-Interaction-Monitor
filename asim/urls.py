
from django.conf.urls import url

from . import views

app_name = 'asim'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'browse/$', views.browse, name='browse'),
    url(r'tgf/$', views.tgf, name='tgf'),
    url(r'orbitdisplay/$', views.orbitdisplay, name='orbitdisplay'),
    url(r'your_location/$', views.your_location, name='your_location'),
    # sample polls/5/
    url(r'^(?P<obsid>[0-9]+)/$', views.detail, name='detail'),
    # sample /polls/5/results/
    url(r'^(?P<obsid>[0-9]+)/results/$', views.results, name='results'),
    # sample /polls/5/vote/
    url(r'^(?P<obsid>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'search/$', views.search, name='search'),
    url(r'name/$', views.get_name, name='name'),
    url(r'^location/$', views.location, name='location'),
    url(r'^location/thanks/$', views.thanks, name='thanks'),
]
