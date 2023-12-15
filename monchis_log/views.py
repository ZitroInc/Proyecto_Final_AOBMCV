from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Post, Posteo_Lista
from .forms import PostForm, BuscarForm


def index(request):
    posts = Post.objects.all()
    contexto = {"posts": posts}
    return render(request, "monchis/index.html", contexto)


def crear_posteo(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = PostForm()
    return render(request, "monchis/crear_posteo.html", {"form": form})


def mostrar_posteo(request):
    if request.method == "POST":
        posteo_form = BuscarForm(request.POST)

        if posteo_form.is_valid():
            busqueda = posteo_form.cleaned_data["buscar"]
            resultados = Post.objects.filter(titulo__icontains=busqueda)

    else:
        resultados = Post.objects.all()
    posteo_form = BuscarForm()

    contexto = {"posteo_form": posteo_form, "resultados": resultados}

    return render(request, "monchis/posteos.html", contexto)


class PosteoLista(ListView):
    model = Posteo_Lista


class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = "monchis/posteos.html"


class PostDetalle(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "monchis/posteos_detalle.html"


class PostCreacion(CreateView):
    model = Post
    sucess_url = "monchis/posteos/listar"
    template_name = "monchis/crear_posteo.html"
    fields = ["nombre_local", "comentario"]


class PostActualizacion(UpdateView):
    model = Post
    success_url = "monchis/posteos/listar"
    template_name = "monchis/crear_posteo.html"
    fields = ["nombre_local", "comentario"]


class PostEliminar(DeleteView):
    model = Post
    template_name = "monchis/eliminar_posteo.html"
    success_url = "monchis/posteos/listar"
