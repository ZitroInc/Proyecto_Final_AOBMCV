from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts.views import edit_avatar_request, edit_user_request, login_request, signup_request

urlpatterns = [
    path('/signup/', signup_request, name="signup"),
    path('/profile/', edit_user_request, name="profile"),
    path('/avatar/', edit_avatar_request, name="avatar"),
    path('/login/', login_request, name="login"),
    path('/logout/', LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
]
