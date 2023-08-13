from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *

#INICIO
def inicio(request):
    noticias = Noticia.objects.all()
    imagenes = Imagen.objects.all()
    if request.user.is_authenticated:
        avatares = Avatar.objects.filter(user=request.user.id)
        if avatares:
            contexto = {"noticias":noticias, 'url':avatares[0].imagen.url, 'avatares':avatares, 'imagen':imagenes[0].imagen.url}

            return render(request, "ContentApp/inicio.html", contexto)
        else:
            contexto = {"noticias":noticias, 'imagen':imagenes[0].imagen.url}

            return render(request, "ContentApp/inicio.html", contexto)
    else:
        contexto = {"noticias":noticias, 'imagen':imagenes[0].imagen.url}

        return render(request, "ContentApp/inicio.html", contexto)

def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()

            mensaje1 = 'Tu cuenta ha sido creada con exito'
            mensaje2 = 'Iniciar sesion'
            url1 = reverse('Login')
            contexto = {'mensaje1':mensaje1, 'mensaje2':mensaje2, 'url1':url1}

            return render(request, "ContentApp/actionDetermination.html", contexto)
    else:
        form = UserRegisterForm()

    return render(request, "ContentApp/signup.html", {'form':form})

def login_request(request):
    if request.user.is_authenticated:
        titulo = 'Inicio de sesion'
        mensaje1 = 'Ya tienes una sesion iniciada'
        mensaje2 = 'Ir a inicio'
        url1 = reverse('Inicio')

        contexto = {'titulo':titulo, 'mensaje1':mensaje1, 'mensaje2':mensaje2, 'url1':url1}

        return render(request, "ContentApp/actionDetermination.html", contexto)
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                usuario = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=usuario, password=password)

                if user is not None:
                    login(request, user)

                    titulo = 'Inicio de sesion'
                    mensaje1 = 'Has iniciado sesion exitosamente'
                    mensaje2 = 'Ir a inicio'
                    url1 = reverse('Inicio')

                    contexto = {'titulo':titulo, 'mensaje1':mensaje1, 'mensaje2':mensaje2, 'url1':url1}

                    return render(request, "ContentApp/actionDetermination.html", contexto)
                else:
                    mensaje = 'Formulario incorrecto'

                    return render(request, "ContentApp/login.html", {'mensaje':mensaje})
            else:
                titulo = 'Error de inicio de sesion'
                mensaje1 = 'Los datos ingresados son incorrectos, intentalo nuevamente.'
                mensaje_url1 = 'Reintentar'
                mensaje_url2 = 'Ir a inicio'
                url1 = reverse('Login')
                url2 = reverse('Inicio')

                contexto = {'titulo':titulo, 'mensaje1':mensaje1, 'url1':url1, 'mensaje_url1':mensaje_url1, 'mensaje_url2':mensaje_url2, 'url2':url2}

            return render(request, "ContentApp/actionDetermination.html", contexto)
        else:
            form = AuthenticationForm()

        return render(request, "ContentApp/login.html", {'form':form})    

#CONTENIDO
def buscarNoticias(request):
    if request.method == 'GET':
        keywords = request.GET.get('keywords')
        if keywords:
            keywords_lower = keywords.lower()
            noticias = Noticia.objects.filter(titulo__icontains=keywords_lower) | \
                       Noticia.objects.filter(subtitulo__icontains=keywords_lower) | \
                       Noticia.objects.filter(cuerpo__icontains=keywords_lower) | \
                       Noticia.objects.filter(autor__icontains=keywords_lower)

            contexto = {'noticias':noticias, 'keywords':keywords_lower}

            return render(request, 'ContentApp/buscarNoticias.html', contexto)

    return render(request, 'ContentApp/buscarNoticias.html')

@login_required
def detalleNoticia(request, noticia_id):
    noticia = Noticia.objects.get(id=noticia_id)
    if request.user.is_authenticated:
        avatares = Avatar.objects.filter(user=request.user.id)
        if avatares:
            contexto = {'noticia':noticia, 'noticia_id':noticia_id, 'url':avatares[0].imagen.url, 'avatares':avatares}

            return render(request, "ContentApp/detalleNoticia.html", contexto)
        else:
            contexto = {'noticia':noticia, 'noticia_id':noticia_id}

            return render(request, "ContentApp/detalleNoticia.html", contexto)
    else:
        contexto = {'noticia':noticia, 'noticia_id':noticia_id}

        return render(request, "ContentApp/detalleNoticia.html", contexto)

@staff_member_required
def crearNoticia(request):
    if request.method == 'POST':
        miFormulario = NoticiaFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            noticia = Noticia(imagen=informacion['imagen'],
                              titulo=informacion['titulo'],
                              subtitulo=informacion['subtitulo'],
                              cuerpo=informacion['cuerpo'],
                              autor=informacion['autor'],
                              fecha=informacion['fecha'])
            noticia.save()

            mensaje1 = 'El articulo ha sido creado exitosamente'
            mensaje2 = 'Volver a noticias'
            url1 = reverse('Pages')

            contexto = {'mensaje1':mensaje1, 'mensaje2':mensaje2, 'url1':url1}  

            return render(request, "ContentApp/actionDetermination.html", contexto)

    else:
        miFormulario = NoticiaFormulario()

    return render(request, "ContentApp/crearNoticia.html", {"miFormulario":miFormulario})

@staff_member_required
def editarNoticia(request, noticia_id):
    noticia = Noticia.objects.get(id=noticia_id)

    if request.method == 'POST':
        miFormulario = NoticiaFormulario(request.POST, request.FILES, instance=noticia)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            noticia.titulo = informacion['titulo']
            noticia.subtitulo = informacion['subtitulo']
            noticia.cuerpo = informacion['cuerpo']
            noticia.autor = informacion['autor']
            noticia.fecha = informacion['fecha']

            noticia.save()

            titulo = 'Articulo editado'
            mensaje1 = 'El articulo ha sido editado exitosamente'
            mensaje2 = 'Volver a noticias'
            url1 = reverse('Pages')
            contexto = {'titulo':titulo, 'mensaje1':mensaje1, 'mensaje2':mensaje2, 'url1':url1}

            return render(request, "ContentApp/actionDetermination.html", contexto)
    else:
        miFormulario = NoticiaFormulario(instance=noticia)
        
    return render(request, "ContentApp/editarNoticia.html", {'miFormulario':miFormulario, 'noticia_id':noticia_id})

@staff_member_required
def eliminarNoticia(request, noticia_id):
    noticia = Noticia.objects.get(id=noticia_id)
    noticia.delete()

    titulo = 'Articulo eliminado'
    mensaje1 = 'El articulo ha sido eliminado exitosamente'
    mensaje2 = 'Volver a noticias'
    url1 = reverse('Pages')
    contexto = {'titulo':titulo, 'mensaje1':mensaje1, 'mensaje2':mensaje2, 'url1':url1}

    return render(request, "ContentApp/actionDetermination.html", contexto)

def pages(request):
    noticias = Noticia.objects.all()
    if request.user.is_authenticated:
        avatares = Avatar.objects.filter(user=request.user.id)
        if avatares:
            contexto = {"noticias":noticias, 'url':avatares[0].imagen.url, 'avatares':avatares}

            return render(request, "ContentApp/pages.html", contexto)
        else:
            contexto = {"noticias":noticias}

            return render(request, "ContentApp/pages.html", contexto)
    else:
        noticias = Noticia.objects.all()

        contexto = {"noticias":noticias}

    return render(request, "ContentApp/pages.html", contexto)

def about(request): 
    if request.user.is_authenticated:
        avatares = Avatar.objects.filter(user=request.user.id)
        if avatares:
            contexto = {'url':avatares[0].imagen.url, 'avatares':avatares}

            return render(request, "ContentApp/about.html", contexto)
        else:
            return render(request, "ContentApp/about.html")
    else:

        return render(request, "ContentApp/about.html")
