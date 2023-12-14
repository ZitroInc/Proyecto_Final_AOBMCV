from django.urls import path
from monchis_log.views import crear_posteo, buscar_posteo, index

urlpatterns = [
    path('postear/', crear_posteo),
    path('buscar/', buscar_posteo),
    path('', index),

]