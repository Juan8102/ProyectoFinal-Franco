from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField(label='Correo electronico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

class NoticiaFormulario(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['imagen', 'titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha']
        help_texts = {k:'' for k in fields}

class ImagenFormulario(forms.Form):
    noticia = forms.ModelChoiceField(queryset=Noticia.objects.all())
    imagen = forms.ImageField(label='Imagen')

    class Meta:
        model = Imagen
        fields = ['imagen']
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.Form):
    username = forms.ModelChoiceField(queryset=User.objects.all())
    imagen = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ['imagen']
        help_texts = {k:"" for k in fields}
