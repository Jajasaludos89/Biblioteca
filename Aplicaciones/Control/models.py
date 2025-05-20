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