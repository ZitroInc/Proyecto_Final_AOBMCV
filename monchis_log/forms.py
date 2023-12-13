from django import forms
from .models import Post, Usuario


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['nombre_local', 'comentario', 'imagen']


class BuscarForm(forms.Form):
    nombre_local = forms.CharField(max_length=100)
    plato = forms.CharField(max_length=50)

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usuario']