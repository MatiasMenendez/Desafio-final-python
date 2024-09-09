from django.db import models

# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    cuerpo = models.CharField(max_length=100)
    autor = models.CharField(max_length=40)
    fecha = models.CharField(max_length=40)
    imagen = models.CharField(max_length=40)
    
    def __str__(self):
     return f"titulo: {self.titulo} - subtitulo: {self.subtitulo} - cuerpo: {self.cuerpo} - autor: {self.autor} - fecha: {self.fecha} - imagen: {self.imagen}" 