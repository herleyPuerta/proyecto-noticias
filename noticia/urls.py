from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('noticia.apps.urls')),
    url(r'^',include('noticia.apps.webServices.wsNoticias.urls')),
    url(r'^media/(?P<path>.*)', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
)
