from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from ContentApp.models import *
from .models import *
from .forms import *

@login_required
def perfil(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        usuario = request.user
        url = reverse('Inicio')

        contexto = {'usuario':usuario, 'url':url, 'avatar':avatares[0].imagen.url}

        return render(request, 'ProfilesApp/perfil.html', contexto)
    else:
        usuario = request.user
        url = reverse('Inicio')

        contexto = {'usuario':usuario, 'url':url}
        
    return render(request, "ProfilesApp/perfil.html", contexto)

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, instance=usuario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']

            usuario.save()

            mensaje1 = 'Has editado tu usuario con exito'
            mensaje2 = 'Ir al perfil'
            url1 = reverse('Perfil')

            contexto = {'mensaje1':mensaje1, 'mensaje2':mensaje2, 'url1':url1, 'usuario':usuario}

            return render(request, "ProfilesApp/actionDetermination.html", contexto)
    else:
        miFormulario = UserEditForm(instance=usuario)

    return render(request, "ProfilesApp/editarPerfil.html", {"miFormulario":miFormulario, 'usuario':usuario})

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            usuario = User.objects.get(username=request.user)
            avatar = Avatar(user=usuario, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()

            mensaje1 = 'Has agregado tu avatar exitosamente'
            mensaje2 = 'Ir al perfil'
            url1 = reverse('Perfil')

            contexto = {'mensaje1':mensaje1, 'mensaje2':mensaje2, 'url1':url1}

            return render(request, "ProfilesApp/actionDetermination.html", contexto)
        else:
            mensaje1 = 'La imagen ingresada no es valida'
            mensaje2 = 'Reintentar'
            url1 = reverse('AgregarAvatar')

            contexto = {'mensaje1':mensaje1, 'mensaje2':mensaje2, 'url1':url1}

            return render(request, 'ProfilesApp/actionDetermination.html', contexto)
    else:
        miFormulario = AvatarFormulario()

        contexto = {'miFormulario':miFormulario}

    return render(request, 'ProfilesApp/agregarAvatar.html', contexto)

@login_required
def editarAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            avatares = Avatar.objects.filter(user=request.user)
            avatares[0].imagen.delete()
            avatares.delete()

            usuario = User.objects.get(username=request.user)
            avatar = Avatar(user=usuario, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()

            mensaje1 = 'Has editado tu avatar exitosamente'
            mensaje2 = 'Ir al perfil'
            url1 = reverse('Perfil')

            contexto = {'mensaje1':mensaje1, 'mensaje2':mensaje2, 'url1':url1}

            return render(request, "ProfilesApp/actionDetermination.html", contexto)
        else:
            mensaje1 = 'La imagen ingresada no es valida'
            mensaje2 = 'Reintentar'
            url1 = reverse('AgregarAvatar')

            contexto = {'mensaje1':mensaje1, 'mensaje2':mensaje2, 'url1':url1}

            return render(request, 'ProfilesApp/actionDetermination.html', contexto)
    else:
        miFormulario = AvatarFormulario()

        contexto = {'miFormulario':miFormulario}

    return render(request, 'ProfilesApp/editarAvatar.html', contexto)

@login_required
def eliminarAvatar(request):
    avatar = Avatar.objects.filter(user=request.user)
    avatar[0].imagen.delete()
    avatar.delete()
        
    mensaje1 = 'Has eliminado tu avatar exitosamente'
    mensaje2 = 'Ir al perfil'
    url1 = reverse('Perfil')

    contexto = {'mensaje1':mensaje1, 'mensaje2':mensaje2, 'url1':url1}

    return render(request, "ProfilesApp/actionDetermination.html", contexto)
