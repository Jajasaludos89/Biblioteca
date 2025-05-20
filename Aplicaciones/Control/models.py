from django.db import models

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20)
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)

    def __str__(self):
        fila = "{0}: {1} - {2}"
        return fila.format(self.codigo, self.titulo, self.autor)
    
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        fila = "{0} - {1}"
        return fila.format(self.cedula, self.nombre)

class Prestamo(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()

    def __str__(self):
        fila = "Préstamo {0} - {1} - {2}"
        return fila.format(self.id, self.usuario.nombre, self.libro.titulo)
    
class Jugador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=200)
    alias = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    posicion = models.CharField(max_length=100)


    def __str__(self):
        fila = "{0}: {1} - {2} - {3} - {4} - {5}"
        return fila.format(self.id, self.nombre, self.apellido, self.alias, self.numero, self.posicion)
    
class Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    alias = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    localizacion = models.CharField(max_length=100)
    fecha_registro = models.DateField()
    

    def __str__(self):
        fila = "Equipo {0} - {1}"
        return fila.format(self.id, self.jugador.nombre)