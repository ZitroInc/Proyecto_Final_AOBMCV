from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts.views import edit_avatar_request, edit_user_request, login_request, signup_request, CustomLogoutView

urlpatterns = [
    # path("signup", signup_request, name="signup"),
    path("signup", signup_request, name="Signup"),
    # path("profile", edit_user_request, name="profile"),
    path("profile", edit_user_request, name="Profile"),
    # path("avatar", edit_avatar_request, name="avatar"),
    path("avatar", edit_avatar_request, name="Avatar"),
    # path("login", login_request, name="login"),
    path("login", login_request, name="Login"),
    # path("logout", LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    path("logout", CustomLogoutView.as_view(), name="Logout"),
]
