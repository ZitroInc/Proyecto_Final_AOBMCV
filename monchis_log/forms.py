from django import forms
from .models import Post, Usuario


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'descripcion', 'imagen']
                                # descripcion del post
"""REVISAR"""
class BuscarForm(forms.Form):
    buscar = forms.CharField(label='Buscar')

# class UsuarioForm(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ['user']