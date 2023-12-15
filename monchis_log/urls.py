from django.urls import path
from monchis_log.views import crear_posteo, mostrar_posteo, index

urlpatterns = [
    path("postear/", crear_posteo, name="postear"),
    path("buscar/", mostrar_posteo, name="buscar"),
    path("", index),
]
