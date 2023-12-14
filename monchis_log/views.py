from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Post, Posteo_Lista
from .forms import PostForm

# def index(request):
#     posts = Post.objects.all()
#     return render(request, 'mochis/index.html', {'posts': posts})
def index(request):
    posts = Post.objects.all()
    contexto = {
        'posts': posts
    }
    return render(request, '', contexto)

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
    nombre_local = request.GET["nombre_local"]


class PosteoLista(ListView):
    model = Posteo_Lista

# def mostrar_posteos(request):


#""" @login_required()"""
# def crear_posteo_form(request):
#     if request.method == "POST":
#         post_formulario = PostForm(request.POST)
#         if post_formulario.is_valid():
#             informacion = post_formulario.cleaned_data
#             post_crear = Post(nombre_local=informacion["nombre_local"], plato=informacion["plato"])
#             crear_posteo_form.save()
#             return redirect("##########cambiar!!!#########")
#
#     post_formulario = PostForm()
#     contexto = {
#         "form": post_formulario
#     }
#     return render(request, "monchis_log/crear_posteo.html", contexto)



