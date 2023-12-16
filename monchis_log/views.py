from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Post

# Posteo_Lista
from .forms import PostForm, BuscarForm


def inicio(request):
    posts = Post.objects.all()
    contexto = {"posts": posts}
    return render(request, "monchis/inicio.html", contexto)


def crear_posteo(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = PostForm()
    return render(request, "monchis/crear_posteo.html", {"form": form})

"""# Test mezclando Búsqueda y Lista"""
# def mostrar_posteo(request):
#     if request.method == "POST":
#         posteo_form = BuscarForm(request.POST)
#
#         if posteo_form.is_valid():
#             busqueda = posteo_form.cleaned_data["buscar"]
#             resultados = Post.objects.filter(titulo__icontains=busqueda)
#
#     else:
#         resultados = Post.objects.all()
#     posteo_form = BuscarForm()
#
#     contexto = {"posteo_form": posteo_form, "resultados": resultados}
#
#     return render(request, "monchis/posteos.html", contexto)

"""Test separado"""

def buscar(request):
    buscar_form = BuscarForm()
    resultados = []

    if request.method == 'POST':
        buscar_form = BuscarForm(request.POST)

        if buscar_form.is_valid():
            buscar = buscar_form.cleaned_data['buscar']
            resultados = Post.objects.filter(subtitulo__icontains=buscar)

    contexto = {
        'busqueda_form': buscar_form,
        'resultados': resultados
    }

    return render(request, 'monchis/buscar.html', contexto)



def posts(request):
    publicaciones = Post.objects.all()
    contexto = {
        'posteos': publicaciones
    }
    return render(request, 'monchis/posteos_lista.html', contexto)



class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = "monchis/posteos_lista.html"
    context_object_name = "posteos"



class PostDetalle(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "monchis/posteos_detalle.html"
#

class PostCreacion(CreateView):
    model = Post
    sucess_url = "/lista_monchis"
    template_name = "monchis/crear_posteo.html"
    fields = ["titulo", "subtitulo", "descripcion", "imagen"]


class PostActualizacion(UpdateView):
    model = Post
    success_url = "/lista_monchis"
    template_name = "monchis/crear_posteo.html"
    fields = ["titulo", "subtitulo", "descripcion", "imagen"]


class PostEliminar(DeleteView):
    model = Post
    template_name = "monchis/eliminar_posteo.html"
    success_url = "monchis/posteos/listar"

def about_us(request):
    return render(request, 'monchis/about_us.html')

