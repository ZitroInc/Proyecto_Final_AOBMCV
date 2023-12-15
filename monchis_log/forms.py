from django import forms

from .models import Post, Comentario,Usuario


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "subtitulo", "descripcion", "imagen"]
        # descripcion del post


class BuscarForm(forms.Form):
    buscar = forms.CharField(label="Buscar")


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ()


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nickname', 'email']
