from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
	user= models.ForeignKey(User,unique=True)
	def __unicode__(self):
		return self.user.first_name+" "+self.user.last_name

class Noticia(models.Model):
	def url(self,filename):
		return "Noticias/%s/%s/%s"%(self.fechaCreada,self.titulo,filename)

	titulo				= models.CharField(max_length=60,null=False,blank=False)
	fechaCreada 		= models.DateField(auto_now_add=True)
	entradilla			= models.TextField(max_length=160,null=False,blank=False)
	contenido			= models.TextField(max_length=3000,null=False,blank=False)
	imagen				= models.ImageField(upload_to=url,null=True,blank=False)
	activo 				= models.BooleanField(default=True,null=False)

	def __unicode__(self):
		return self.titulo