from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login




# Create your views here.

def new_user(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)       """EDITABLES"""

        if form.is_valid():
            form.save()

            return redirect("")                     """REVISAR"""

    form = UserRegisterForm()
    contexto = {
        "form": form
    }
    return render(request, "", contexto)    """REVISAR"""