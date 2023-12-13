from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts.views import edit_avatar_request, edit_user_request, login_request, signup_request

urlpatterns = [
    path('signup/', signup_request, name="Registrarse"),
    path('editar/', edit_user_request, name="Editar"),
    path('avatar/', edit_avatar_request, name="Avatar"),
    path('login/', login_request, name="Login"),
    path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name="Logout"),
]
