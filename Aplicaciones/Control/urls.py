from django.urls import path
from . import views

urlpatterns = [
    # Libros
    path('', views.inicio),
    path('nuevoLibro', views.nuevoLibro),
    path('guardarLibro', views.guardarLibro),
    path('eliminarLibro/<int:id>', views.eliminarLibro),
    path('editarLibro/<int:id>', views.editarLibro),
    path('procesarEdicionLibro', views.procesarEdicionLibro),

]