from django.contrib.auth.forms import UserCreationForm, User, UserChangeForm
from django import forms
from accounts.models import Avatar


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email")


# class UserUpdateForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ("username", "email")


class UserUpdateForm(UserChangeForm):
    avatar = forms.ImageField(required=False, label="Avatar")

    class Meta:
        model = User
        fields = ("username", "email", "avatar")


class AvatarUpdateForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ("image",)
