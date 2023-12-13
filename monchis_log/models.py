from django.db import models

# Create your models here.
class Post(models.Model):
    nombre_local = models.CharField(max_length=100)
    comentario = models.TextField()
    imagen = models.ImageField(upload_to='uploads/')
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_local

