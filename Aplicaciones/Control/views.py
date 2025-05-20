from django.shortcuts import render, redirect
from .models import Libro, Usuario, Prestamo
from django.contrib import messages  

#LIBROS

def inicio(request):
    listadoLibros = Libro.objects.all()
    return render(request, "inicio.html", {'libros': listadoLibros})

def nuevoLibro(request):
    return render(request, "nuevoLibro.html")

def guardarLibro(request):
    codigo = request.POST["codigo"]
    titulo = request.POST["titulo"]
    autor = request.POST["autor"]

    Libro.objects.create(codigo=codigo, titulo=titulo, autor=autor)
    messages.success(request, "Libro GUARDADO exitosamente")
    return redirect('/')

def eliminarLibro(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    messages.success(request, "Libro ELIMINADO exitosamente")
    return redirect('/')

def editarLibro(request, id):
    libro = Libro.objects.get(id=id)
    return render(request, "editarLibro.html", {'libroEditar': libro})

def procesarEdicionLibro(request):
    id = request.POST["id"]
    codigo = request.POST["codigo"]
    titulo = request.POST["titulo"]
    autor = request.POST["autor"]

    libro = Libro.objects.get(id=id)
    libro.codigo = codigo
    libro.titulo = titulo
    libro.autor = autor
    libro.save()

    messages.success(request, "Libro ACTUALIZADO exitosamente")
    return redirect('/')