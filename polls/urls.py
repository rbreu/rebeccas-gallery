from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from polls.models import Poll

urlpatterns = patterns('',
                       url(r'^$',
                           ListView.as_view(
            queryset=Poll.objects.order_by('-published_at')[:5],
            context_object_name='latest_poll_list',
            template_name='polls/index.html'),
                           name="polls"),
                       
                       url(r'^(?P<pk>\d+)/$',
                           DetailView.as_view(
            model=Poll,
            template_name='polls/detail.html')),
                       
                       url(r'^(?P<pk>\d+)/results/$',
                           DetailView.as_view(
            model=Poll,
            template_name='polls/results.html'),
                           name='poll_results'),
                       
                       url(r'^(?P<id>\d+)/vote/$', 'polls.views.vote'),
                       )
