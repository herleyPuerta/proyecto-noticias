from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('noticia.apps.views',
    url(r'^$', 'index_view', name='vistaPrincipal'),
    url(r'^add/noticia/$','nueva_noticia_view',name='vista_nueva_noticia'),
    url(r'^edit/noticia/(?P<id_not>.*)/$','edit_noticia_view',name="vista_editar_noticia"),
    url(r'^delete/noticia/(?P<id_not>.*)/$','delete_noticia_view',name="vista_eliminar_noticia"),
    url(r'^noticia/(?P<id_not>.*)/$','singleNoticia_view', name='vista_single_noticia'),
    url(r'^login/$', 'login_view', name='vistaLogin'),
    url(r'^logout/$', 'logout_view', name='vistaLogout'),
    url(r'^noticias/$','noticias_view',name='vistaNoticias'),    
)