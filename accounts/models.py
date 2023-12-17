from django.contrib.auth.models import User
from django.db import models


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/avatares", null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.image}"
