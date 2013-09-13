from django import forms

class editNoticiaForm(forms.Form):
	titulo 		= forms.CharField(widget=forms.TextInput(),required=True)
	entradilla  = forms.CharField(widget=forms.Textarea,required=True)
	contenido	= forms.CharField(widget=forms.Textarea,required=True)
	imagen		= forms.ImageField(required=False)

	#valida informacion para que no haya informacion erronea
	def clean(self):
		return self.cleaned_data
class ContactForm(forms.Form):
	Email	= forms.EmailField(widget=forms.TextInput())
	Titulo	= forms.CharField(widget=forms.TextInput())
	Texto	= forms.CharField(widget=forms.Textarea)