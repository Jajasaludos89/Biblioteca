from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('nuevoLibro', views.nuevoLibro),
    path('guardarLibro', views.guardarLibro),
    path('eliminarLibro/<int:id>', views.eliminarLibro),
    path('editarLibro/<int:id>', views.editarLibro),
    path('procesarEdicionLibro', views.procesarEdicionLibro),

    path('usuarios', views.usuarios),
    path('nuevoUsuario', views.nuevoUsuario),
    path('guardarUsuario', views.guardarUsuario),
    path('eliminarUsuario/<int:id>', views.eliminarUsuario),
    path('editarUsuario/<int:id>', views.editarUsuario),
    path('procesarEdicionUsuario', views.procesarEdicionUsuario),

    path('prestamos', views.prestamos),
    path('nuevoPrestamo', views.nuevoPrestamo),
    path('guardarPrestamo', views.guardarPrestamo),
    path('eliminarPrestamo/<int:id>', views.eliminarPrestamo),
    path('editarPrestamo/<int:id>', views.editarPrestamo),
    path('procesarEdicionPrestamo', views.procesarEdicionPrestamo),

]