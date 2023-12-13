from django import forms
from .models import Post, Usuario


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['nombre_local', 'comentario', 'imagen']


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usuario']