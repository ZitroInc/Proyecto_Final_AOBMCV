from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import PostForm, BuscarForm, ComentarioForm
from .models import Post


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


def buscar(request):
    buscar_form = BuscarForm()
    resultados = []

    if request.method == "POST":
        buscar_form = BuscarForm(request.POST)

        if buscar_form.is_valid():
            buscar = buscar_form.cleaned_data["buscar"]
            resultados = Post.objects.filter(subtitulo__icontains=buscar)

    contexto = {"busqueda_form": buscar_form, "resultados": resultados}

    return render(request, "monchis/buscar.html", contexto)


def posts(request):
    publicaciones = Post.objects.all()
    contexto = {"posteos": publicaciones}
    return render(request, "monchis/posteos_lista.html", contexto)


class PostList(ListView):
    model = Post
    template_name = "monchis/posteos_lista.html"
    context_object_name = "posteos"


class PostDetalle(DetailView):
    model = Post
    template_name = "monchis/posteos_detalle.html"



class PostCreacion(LoginRequiredMixin, CreateView):
    model = Post
    sucess_url = "/lista_monchis"
    template_name = "monchis/crear_posteo.html"
    fields = ["titulo", "subtitulo", "descripcion", "imagen"]


class PostActualizacion(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = "/lista_monchis"
    template_name = "monchis/crear_posteo.html"
    form_class = PostForm

    def form_valid(self, form):
        post = form.save(commit=False)
        if "imagen" in form.changed_data:
            post.imagen = form.cleaned_data["imagen"]
        post.save()
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.usuario.user


class PostEliminar(DeleteView):
    model = Post
    template_name = "monchis/eliminar_posteo.html"
    success_url = "monchis/posteos/listar"


def about_us(request):
    return render(request, "monchis/about_us.html")


class AgregarComentarioView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        form = ComentarioForm(request.POST)

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()

        return redirect("DetallesPost", pk=post_id)
