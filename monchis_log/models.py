from django.db import models


# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="media/foto_post/")
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_local


class Usuario(models.Model):
    nickname = models.CharField(max_length=30)
    email = models.EmailField()


class Posteo_Lista(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)


class Comentario(models.Model):
    # nickname
    comment = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
