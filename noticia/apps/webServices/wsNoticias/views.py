from django.http import HttpResponse
from noticia.apps.models import Noticia
from django.core import serializers

def wsNoticias_view(request):
	data	= serializers.serialize("json",Noticia.objects.filter(activo=True))
	return HttpResponse(data,mimetype="application/json")
