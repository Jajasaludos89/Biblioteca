from django.db import models

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20)
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)

    def __str__(self):
        fila = "{0}: {1} - {2}"
        return fila.format(self.codigo, self.titulo, self.autor)
