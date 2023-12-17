from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    titulo = models.CharField(max_length=100)                       # Nombre del Local de comida
    subtitulo = models.CharField(max_length=100)                    # Para comentar el tipo de comida que se encuentra
    descripcion = models.TextField()                                # Descripción en detalle
    imagen = models.ImageField(upload_to="media/foto_post/")        # Foto de la comida o el local
    fecha = models.DateTimeField(auto_now_add=True)
    # username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30)          #"""REVISAR"""
    first_name = models.CharField(max_length=30)         # """REVISAR"""
    last_name = models.CharField(max_length=30)          #"""REVISAR"""
    email = models.EmailField()


class Posteo_Lista(models.Model):                           #Solo se muestran estos dos, para dar a los visitantes una idea de lo que verán en la descripción detallada
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)


class Comentario(models.Model):
    comment = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
