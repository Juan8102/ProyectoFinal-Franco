from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ContentApp.models import *
from django import forms

class UserEditForm(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario")
    email = forms.CharField(label="Email")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

class AvatarFormulario(forms.ModelForm):
    imagen = forms.ImageField()

    class Meta:
        model = Avatar
        fields = ['imagen']
        help_texts = {k:"" for k in fields}
