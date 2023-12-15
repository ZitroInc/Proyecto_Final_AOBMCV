from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

from accounts.forms import UserRegisterForm, UserUpdateForm, AvatarUpdateForm
from accounts.models import Avatar

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('Inicio')


def signup_request(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect("Profile")

    form = UserRegisterForm()
    contexto = {"form": form}
    return render(request, "accounts/signup.html", contexto)

@login_required
def edit_user_request(request):
    user = request.user
    if request.method == "POST":
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.save()
            return redirect("Avatar")

    form = UserUpdateForm(initial={"email": user.email})
    contexto = {"form": form}
    return render(request, "accounts/profile.html", contexto)


@login_required
def edit_avatar_request(request):
    user = request.user
    if request.method == "POST":
        form = AvatarUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            try:
                avatar = user.avatar
                avatar.image = data["image"]
            except:
                avatar = Avatar(user=user, image=data["image"])
            avatar.save()

            return redirect("Inicio")

    form = AvatarUpdateForm()
    contexto = {"form": form}
    return render(request, "accounts/avatar.html", contexto)


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get("username")
            contrasenia = data.get("password")

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)

        return redirect("Inicio")

    form = AuthenticationForm()
    contexto = {"form": form}
    return render(request, "accounts/login.html", contexto)
