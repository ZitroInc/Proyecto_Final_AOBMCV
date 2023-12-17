from django.urls import path
from monchis_log.views import (
    crear_posteo,
    inicio,
    posts,
    buscar,
    about_us,
    AgregarComentarioView, PostDetalle
)

urlpatterns = [
    path("postear/", crear_posteo, name="Postear"),
    path("about_us/", about_us, name="about_us"),
    path("buscar/", buscar, name="Buscar"),
    path("lista_monchis/", posts, name="ListaPosteos"),
    path("", inicio, name="Inicio"),
    path("detalles/<int:pk>/", PostDetalle.as_view(), name="Detalles"),
    path(r"^detalles/(?P<pk>\d+)$", PostDetalle.as_view(), name="Detalles"),
    # path("detalles/<int:post_id>/", AgregarComentarioView.as_view, name="AgregarComentario"),
]
