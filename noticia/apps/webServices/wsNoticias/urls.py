from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('noticia.apps.webServices.wsNoticias.views',
	url(r'^ws/noticias/$','wsNoticias_view',name="ws_noticias_url"),
)