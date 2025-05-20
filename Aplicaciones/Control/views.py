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

#Usuario

def usuarios(request):
    listadoUsuarios = Usuario.objects.all()
    return render(request, "usuarios.html", {'usuarios': listadoUsuarios})

def nuevoUsuario(request):
    return render(request, "nuevoUsuario.html")

def guardarUsuario(request):
    nombre = request.POST["nombre"]
    cedula = request.POST["cedula"]
    direccion = request.POST["direccion"]

    Usuario.objects.create(nombre=nombre, cedula=cedula, direccion=direccion)
    messages.success(request, "Usuario GUARDADO exitosamente")
    return redirect('/usuarios')

def eliminarUsuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    messages.success(request, "Usuario ELIMINADO exitosamente")
    return redirect('/usuarios')

def editarUsuario(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, "editarUsuario.html", {'usuarioEditar': usuario})

def procesarEdicionUsuario(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    cedula = request.POST["cedula"]
    direccion = request.POST["direccion"]

    usuario = Usuario.objects.get(id=id)
    usuario.nombre = nombre
    usuario.cedula = cedula
    usuario.direccion = direccion
    usuario.save()

    messages.success(request, "Usuario ACTUALIZADO exitosamente")
    return redirect('/usuarios')
