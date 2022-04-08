from django import forms
from django.contrib.auth.models import User, Permission, Group

from rentcar_app.models import Profile


class LoginForm(forms.Form):  # Form connected with login
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class CreateUserForm(forms.ModelForm):  # Form allows to create a new user
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        widgets = {'password': forms.PasswordInput()}


class UpdateGroupPermissionForm(forms.ModelForm):  # Form allows to edit Group permissions by user who has permission for that (superuser)
    class Meta:
        model = Group
        fields = ['name', 'permissions']
        widgets = {
            'permissions': forms.CheckboxSelectMultiple()
        }
