from django.urls import path, include
from ProfilesApp import views

urlpatterns = [
    path('accounts/profile', views.perfil, name='Perfil'),
    path('accounts/editarPerfil', views.editarPerfil, name='EditarPerfil'),
    path('accounts/agregarAvatar', views.agregarAvatar, name='AgregarAvatar'),
    path('accounts/editarAvatar', views.editarAvatar, name='EditarAvatar'),
    path('accounts/eliminarAvatar', views.eliminarAvatar, name='EliminarAvatar'),

    path('../', views.perfil, name='Inicio'),
]