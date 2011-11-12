from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from images.models import Tag, Image

urlpatterns = patterns('',
                       url(r'^$',
                           ListView.as_view(
            queryset=Image.objects.order_by('-publication_date'),
            template_name='images/index.html')),

                       url(r'^(?P<pk>\d+)/$',
                           DetailView.as_view(
            model=Image,
            template_name='images/detail.html'),
                           name="image_detail"),

                       url(r'^tags/$',
                           ListView.as_view(
            queryset=Tag.objects.order_by('label'),
            template_name='images/tag_index.html')),

                       url(r'^tags/(?P<pk>\d+)/$',
                           DetailView.as_view(
            model=Tag,
            template_name='images/tag_detail.html'),
                           name="tag_detail"),
                        )
