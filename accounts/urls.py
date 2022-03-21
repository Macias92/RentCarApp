from django.contrib import admin
from django.urls import path, include
from accounts import views
from accounts.views import LoginView, LogoutView, CreateUserView, UpdateUserPermissionView, UpdateGroupPermissionView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create_user/', CreateUserView.as_view(), name='create_user'),
    path('update_perms/<int:user_id>/', UpdateUserPermissionView.as_view(), name='update_permissions'),
    path('update_group_perms/<int:group_id>/', UpdateGroupPermissionView.as_view(), name='update_group_permissions'),

    ]
