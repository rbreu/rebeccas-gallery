from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'main.views.index'),
                       url(r'^polls/', include('polls.urls')),
                       url(r'^images/', include('images.urls')),
                       url(r'^admin/filebrowser/', include('filebrowser.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

