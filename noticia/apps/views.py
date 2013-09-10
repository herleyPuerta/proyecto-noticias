from django.shortcuts import render_to_response
from django.template import RequestContext 
from django.http import HttpResponseRedirect
from noticia.apps.models import Usuario,Noticia
from django.contrib.auth import login, authenticate, logout
from noticia.apps.forms import editNoticiaForm

def index_view(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/add/noticia')
	else:
		return HttpResponseRedirect('/login')


def login_view(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		usuario = authenticate(username=username, password=password)
		if usuario is not None:
			if usuario.is_active:
				login(request,usuario)
				return HttpResponseRedirect('/')
			else:
				return render_to_response('noactivo.html',locals(),context_instance=RequestContext(request))
		else:
			return render_to_response('nousuario.html',locals(),context_instance=RequestContext(request))
	else:
		return render_to_response('login.html', locals(), context_instance = RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def noticias_view(request):
	noticias = Noticia.objects.all()
	return render_to_response('noticias.html', locals(),context_instance=RequestContext(request))

def nueva_noticia_view(request):
	if request.method == 'POST':
		titulo		= request.POST['titulo']
		entradilla	= request.POST['entradilla']
		contenido	= request.POST['contenido']
		imagen		= request.FILES['imagen']
		noticia 	= Noticia(titulo=titulo,entradilla=entradilla,contenido=contenido,imagen=imagen)
		noticia.save()
		return HttpResponseRedirect('/')
	else:
		return render_to_response('nuevanoticia.html',context_instance=RequestContext(request))


def edit_noticia_view(request, id_not):
	noticia = Noticia.objects.get(id=id_not)
	if request.method == "POST":
		form = editNoticiaForm(request.POST,request.FILES)
		if form.is_valid():
			titulo = form.cleaned_data['titulo']
			entradilla = form.cleaned_data['entradilla']
			contenido = form.cleaned_data['contenido']
			imagen = form.cleaned_data['imagen']
			noticia.titulo = titulo
			noticia.entradilla = entradilla
			noticia.contenido = contenido
			if imagen:
				noticia.imagen = imagen
			noticia.save() #se guarda el modelo editado
			return HttpResponseRedirect('/noticias')
	if request.method == "GET":
		form = editNoticiaForm(initial={
								'titulo' 		: noticia.titulo,
								'entradilla' 	: noticia.entradilla,
								'contenido' 	: noticia.contenido, 
			})
	ctx = {'form':form,'noticia':noticia}
	return render_to_response('editNoticia.html',ctx, context_instance=RequestContext(request))

def delete_noticia_view(request, id_not):
	try:
		noticia = Noticia.objects.get(id=id_not)
		noticia.delete()
	except Exception, e:
		pass
	return HttpResponseRedirect("/noticias")


def singleNoticia_view(request,id_not):
	noticia = Noticia.objects.get(id=id_not)
	ctx = {'noticia':noticia}
	return render_to_response('singleNoticia.html',ctx,context_instance=RequestContext(request))