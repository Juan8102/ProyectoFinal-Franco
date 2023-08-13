from django.urls import path, include
from ContentApp import views

urlpatterns = [
    #INICIO
    path('', views.inicio, name='Inicio'),
    path('accounts/signup', views.signup, name='Signup'),
    path('accounts/login', views.login_request, name='Login'),
    path('logout', views.LogoutView.as_view(), name='Logout'),

    #CONTENIDO
    path('pages/', views.pages, name='Pages'),
    path('pages/buscar/', views.buscarNoticias, name='BuscarNoticias'),
    path('pages/crearNoticia', views.crearNoticia, name='CrearNoticia'),
    path('pages/editarNoticia/<noticia_id>', views.editarNoticia, name='EditarNoticia'),
    path('pages/detalleNoticia/<noticia_id>', views.detalleNoticia, name='DetalleNoticia'),
    path('pages/eliminarNoticia/<noticia_id>', views.eliminarNoticia, name='EliminarNoticia'),
    path('about', views.about, name='About'),

    #PERFILES
    path('ProfilesApp/', include('ProfilesApp.urls')),
]
