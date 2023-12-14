from django.urls import path
from monchis_log.views import index, crear_posteo, buscar_posteo

urlpatterns = [
    path('postear/', crear_posteo),
    path('buscar/', buscar_posteo),
    path('posteos/lista', poste),

]
