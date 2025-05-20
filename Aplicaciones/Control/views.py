from django.shortcuts import render, redirect
from .models import Libro, Usuario, Prestamo, Jugador, Equipo
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

#Prestamos

def prestamos(request):
    listadoPrestamos = Prestamo.objects.all()
    return render(request, "prestamos.html", {'prestamos': listadoPrestamos})

def nuevoPrestamo(request):
    libros = Libro.objects.all()
    usuarios = Usuario.objects.all()
    return render(request, "nuevoPrestamo.html", {'libros': libros, 'usuarios': usuarios})

def guardarPrestamo(request):
    usuario_id = request.POST["usuario"]
    libro_id = request.POST["libro"]
    fecha = request.POST["fecha_prestamo"]

    usuario = Usuario.objects.get(id=usuario_id)
    libro = Libro.objects.get(id=libro_id)

    Prestamo.objects.create(usuario=usuario, libro=libro, fecha_prestamo=fecha)
    messages.success(request, "Préstamo REGISTRADO exitosamente")
    return redirect('/prestamos')

def eliminarPrestamo(request, id):
    prestamo = Prestamo.objects.get(id=id)
    prestamo.delete()
    messages.success(request, "Préstamo ELIMINADO exitosamente")
    return redirect('/prestamos')

def editarPrestamo(request, id):
    prestamo = Prestamo.objects.get(id=id)
    libros = Libro.objects.all()
    usuarios = Usuario.objects.all()
    return render(request, "editarPrestamo.html", {
        'prestamoEditar': prestamo,
        'libros': libros,
        'usuarios': usuarios
    })

def procesarEdicionPrestamo(request):
    id = request.POST["id"]
    usuario_id = request.POST["usuario"]
    libro_id = request.POST["libro"]
    fecha = request.POST["fecha_prestamo"]

    prestamo = Prestamo.objects.get(id=id)
    prestamo.usuario = Usuario.objects.get(id=usuario_id)
    prestamo.libro = Libro.objects.get(id=libro_id)
    prestamo.fecha_prestamo = fecha
    prestamo.save()

    messages.success(request, "Préstamo ACTUALIZADO exitosamente")
    return redirect('/prestamos')

#Jugador


def jugadores(request):
    listadoJugadores = Jugador.objects.all()
    return render(request, "jugadores.html", {'jugadores': listadoJugadores})

def nuevoJugador(request):
    return render(request, "nuevoJugador.html")

def guardarJugador(request):
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    alias = request.POST["alias"]
    numero = request.POST["numero"]
    posicion = request.POST["posicion"]

    Jugador.objects.create(nombre=nombre, apellido=apellido, alias=alias, numero=numero, posicion=posicion)
    messages.success(request, "Jugador GUARDADO exitosamente")
    return redirect('/jugadores')

def eliminarJugador(request, id):
    jugador = Jugador.objects.get(id=id)
    jugador.delete()
    messages.success(request, "Jugador ELIMINADO exitosamente")
    return redirect('/jugadores')

def editarJugador(request, id):
    jugador = Jugador.objects.get(id=id)
    return render(request, "editarJugador.html", {'jugadorEditar': jugador})

def procesarEdicionJugador(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    alias = request.POST["alias"]
    numero = request.POST["numero"]
    posicion = request.POST["posicion"]

    jugador = Jugador.objects.get(id=id)
    jugador.nombre = nombre
    jugador.apellido = apellido
    jugador.alias = alias
    jugador.numero = numero
    jugador.posicion = posicion
    jugador.save()

    messages.success(request, "Jugador ACTUALIZADO exitosamente")
    return redirect('/jugadores')

#Equipo 


def equipos(request):
    listadoEquipos = Equipo.objects.all()
    return render(request, "equipos.html", {'equipos': listadoEquipos})

def nuevoEquipo(request):
    jugadores = Jugador.objects.all()
    return render(request, "nuevoEquipo.html", {'jugador': jugadores})

def guardarEquipo(request):
    jugador_id = request.POST["jugador"]
    nombre = request.POST["nombre"]
    alias = request.POST["alias"]
    director = request.POST["director"]
    localizacion = request.POST["localizacion"]
    fecha = request.POST["fecha_registro"]

    jugador = Jugador.objects.get(id=jugador_id)

    Equipo.objects.create(jugador=jugador, nombre=nombre, alias=alias, director=director, localizacion=localizacion, fecha_registro=fecha)
    messages.success(request, "Equipo REGISTRADO exitosamente")
    return redirect('/equipos')

def eliminarEquipo(request, id):
    equipo = Equipo.objects.get(id=id)
    equipo.delete()
    messages.success(request, "Equipo ELIMINADO exitosamente")
    return redirect('/equipos')

def editarEquipo(request, id):
    equipo = Equipo.objects.get(id=id)
    jugadores = Jugador.objects.all()
    return render(request, "editarJugador.html", {
        'equipoEditar': equipo,
        'jugadores': jugadores
    })

def procesarEdicionEquipo(request):
    id = request.POST["id"]
    jugador_id = request.POST["jugador"]
    nombre = request.POST["nombre"]
    alias = request.POST["alias"]
    director = request.POST["director"]
    localizacion = request.POST["localizacion"]

    fecha = request.POST["fecha_registro"]

    equipo = Equipo.objects.get(id=id)
    equipo.jugador = Jugador.objects.get(id=jugador_id)

    equipo.nombre = nombre
    equipo.alias = alias
    equipo.director = director
    equipo.localizacion = localizacion

    equipo.fecha_prestamo = fecha
    equipo.save()

    messages.success(request, "Equipo ACTUALIZADO exitosamente")
    return redirect('/equipos')
