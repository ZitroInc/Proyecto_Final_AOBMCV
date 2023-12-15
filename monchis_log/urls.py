from django.urls import path
# from monchis_log.views import crear_posteo, mostrar_posteo, inicio
from monchis_log.views import crear_posteo, inicio, posts, buscar #about_us

urlpatterns = [
    path("postear/", crear_posteo, name="Postear"),
    # path("buscar/", mostrar_posteo, name="Buscar"),
    path("buscar/", buscar, name="Buscar"),
    path("lista_monchis/", posts, name="ListaPosteos"),
    path("", inicio, name="Inicio"),
    # path("about", about_us, name="About"),

]
# <h1 class="mb-5">Atte: <a href="{% url About %}">Equipo Monchis</a> </h1>
