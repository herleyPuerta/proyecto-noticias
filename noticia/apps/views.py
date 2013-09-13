from django.shortcuts import render_to_response
from django.template import RequestContext 
from django.http import HttpResponseRedirect
from noticia.apps.models import Usuario,Noticia
from django.contrib.auth import login, authenticate, logout
from noticia.apps.forms import editNoticiaForm,ContactForm
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator,EmptyPage,InvalidPage

def index_view(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/add/noticia')
	else:
		return HttpResponseRedirect('/login')


def login_view(request):
	try:
		if request.method == "POST":
			username = request.POST['username']
			password = request.POST['password']
			usuario = authenticate(username=username, password=password)
			if usuario is not None and usuario.is_active:
				login(request,usuario)
				return HttpResponseRedirect('/')
			loginFailed = True
	except:
		return HttpResponseRedirect('/')
	loginFailed = True
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
		return HttpResponseRedirect('/noticias')
	else:
		return render_to_response('nuevanoticia.html',context_instance=RequestContext(request))
		
def edit_noticia_view(request,id_not):
	try:		
		noticia = Noticia.objects.get(id=id_not)
		if request.method == 'POST':
			if noticia:
				titulo = request.POST['titulo']
				entradilla = request.POST['entradilla']
				contenido	= request.POST['contenido']
				imagen		= request.POST['imagen']
				noticia.titulo = titulo
				noticia.entradilla = entradilla
				noticia.contenido = contenido
				if imagen:
					noticia.imagen = imagen
				noticia.save()
				return HttpResponseRedirect('/noticias')
		else:
			ctx = {'noticia':noticia}
			return render_to_response('editNoticia.html',ctx,context_instance=RequestContext(request))
	except Noticia.DoesNotExist:
		return HttpResponseRedirect("/noticias")

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

def contacto_view(request):
	info_enviado = False
	email = ""
	titulo = ""
	texto = ""
	if request.method == "POST":
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['Email']
			titulo = formulario.cleaned_data['Titulo']
			texto = formulario.cleaned_data['Texto']
			# configuracion usando Gmail
			to_admin = 'pruebadjango1@gmail.com'
			html_content = "informacion recibida de [%s]<br>***Mensaje*** <br>%s"%(email,texto)
			msg = EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html')
			msg.send()
	else:
		formulario = ContactForm()
	ctx = {'form':formulario,'email':email,'titulo':titulo,'texto':texto,  'info_enviado':info_enviado}
	return render_to_response('contacto.html',ctx,context_instance=RequestContext(request))