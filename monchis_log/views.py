from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Posteo_Lista
from .forms import PostForm, BuscarForm


# def index(request):
#     posts = Post.objects.all()
#     return render(request, 'mochis/index.html', {'posts': posts})
def index(request):
    posts = Post.objects.all()
    contexto = {
        'posts': posts
    }
    return render(request, 'monchis/index.html', contexto)

def crear_posteo(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'monchis/crear_posteo.html', {'form': form})

def buscar_posteo(request):
    posteo_form = BuscarForm()
    resultados = []

    if request.method == 'POST':
        posteo_form = BuscarForm(request.POST)

        if posteo_form.is_valid():
            busqueda = posteo_form.cleaned_data['busqueda']
            resultados = Post.objects.filter(nombre_local__icontains=busqueda)

    contexto = {
        'posteo_form': posteo_form,
        'resultados': resultados
    }

    return render(request, 'monchis/buscar.html', contexto)

class PosteoLista(ListView):
    model = Posteo_Lista

# def mostrar_posteos(request):


""" @login_required()"""
def crear_posteo_form(request):
    if request.method == "POST":
        post_formulario = PostForm(request.POST)
        if post_formulario.is_valid():
            informacion = post_formulario.cleaned_data
            crear_posteo = Post(nombre_local=informacion["nombre_local"], plato=informacion["plato"])
            crear_posteo_form.save()
            return redirect("monchis/posteos/")

    post_formulario = PostForm()
    contexto = {
        "form": post_formulario
    }
    return render(request, "monchis/crear_posteo.html", contexto)

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

