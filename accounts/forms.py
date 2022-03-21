from django import forms
from django.contrib.auth.models import User, Permission, Group


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {'password': forms.PasswordInput()}


class UpdateUserPermissionForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'user_permissions']
        widgets = {
            'user_permissions': forms.CheckboxSelectMultiple
        }


class UpdateGroupPermissionForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'permissions']
        widgets = {
            'permissions': forms.CheckboxSelectMultiple
        }
