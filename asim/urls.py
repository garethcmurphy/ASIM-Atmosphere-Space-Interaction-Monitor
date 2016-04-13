
from django.conf.urls import url

from . import views

app_name = 'asim'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'browse/$', views.browse, name='browse'),
    # ex: /polls/5/
    url(r'^(?P<obsid>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<obsid>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<obsid>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'search/$', views.search, name='search'),
    url(r'name/$', views.get_name, name='name'),
]
