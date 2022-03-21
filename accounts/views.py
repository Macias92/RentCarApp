from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.views import View
from accounts.forms import LoginForm, CreateUserForm, UpdateUserPermissionForm, UpdateGroupPermissionForm


# Create your views here.


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                redirect_url = request.GET.get('next', '/')  # pobierze co jest w url po 'next' i tam bedzie przekierowywać, jeżeli tego nie ma to przekierowuje na '/'
                return redirect(redirect_url)
            else:
                return render(request, 'form.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class CreateUserView(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            group = Group.objects.get(name='client')
            user.groups.add(group)
            return redirect('/')
        return render(request, 'form.html', {'form': form})


class UpdateUserPermissionView(View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        form = UpdateUserPermissionForm(instance=user)
        return render(request, 'form.html', {'form': form})

    def post(self, request, user_id):
        user = User.objects.get(pk=user_id)
        form = UpdateUserPermissionForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return render(request, 'form.html', {'form': form})


class UpdateGroupPermissionView(View):
    def get(self, request, group_id):
        group = Group.objects.get(pk=group_id)
        form = UpdateGroupPermissionForm(instance=group)
        return render(request, 'form.html', {'form': form})

    def post(self, request, group_id):
        group = Group.objects.get(pk=group_id)
        form = UpdateGroupPermissionForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
        return render(request, 'form.html', {'form': form})


