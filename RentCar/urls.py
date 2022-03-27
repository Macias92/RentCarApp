"""RentCar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rentcar_app.views import CarAddCreateView, CarUpdateView, IndexView, CarDetailsView, CarDeleteView, \
    contact, RentCarView, car_list, RentListView, RentDetailsView, RentEditView, RentDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', IndexView.as_view(), name='index'),
    path('car_add/', CarAddCreateView.as_view(), name='car_add'),
    path('car_list/', car_list, name='car_list'),
    path('car_details/<int:pk>/', CarDetailsView.as_view(), name='car_details'),
    path('car_update/<int:pk>/', CarUpdateView.as_view(), name='car_update'),
    path('car_delete/<int:pk>/', CarDeleteView.as_view(), name='car_delete'),
    path('rent_add/', RentCarView.as_view(), name='car_rent'),
    path('rent_list/', RentListView.as_view(), name='rent_list'),
    path('rent_details/<int:pk>/', RentDetailsView.as_view(), name='rent_details'),
    path('rent_edit/<int:pk>/', RentEditView.as_view(), name='rent_edit'),
    path('rent_delete/<int:pk>/', RentDeleteView.as_view(), name='rent_delete'),
    path('contact/', contact, name='contact')
]
