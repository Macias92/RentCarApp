from django.contrib import admin
from django.urls import path, include
from accounts.views import LoginView, LogoutView, CreateUserView, UpdateGroupPermissionView, ProfileDetailsView, \
    ProfileUpdateView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create_user/', CreateUserView.as_view(), name='create_user'),
    path('update_group_perms/<int:group_id>/', UpdateGroupPermissionView.as_view(), name='update_group_permissions'),
    path('profile_details/<int:pk>/', ProfileDetailsView.as_view(), name='profile_details'),
    path('profile_update/<int:pk>/', ProfileUpdateView.as_view(), name='profile_update'),

]
