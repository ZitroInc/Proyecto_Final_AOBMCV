from django.urls import path
from monchis_log.views import index, crear_posteo, buscar_posteo

path('Postear/', crear_posteo),
path('Buscar/', buscar_posteo),
path('posteos/lista', poste)
from django.urls import path
from monchis_log.views import index, crear_posteo, buscar_posteo

path('Postear/', crear_posteo),
path('Buscar/', buscar_posteo),
path('posteos/lista', poste)
