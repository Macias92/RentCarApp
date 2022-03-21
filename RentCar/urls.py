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

from rentcar_app.views import CarAddCreateView, CarListView, CarUpdateView, IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', IndexView.as_view(), name='index'),
    path('car_add/', CarAddCreateView.as_view(), name='car_add'),
    path('car_list/', CarListView.as_view(), name='car_list'),
    path('car_update/<int:pk>/', CarUpdateView.as_view(), name='car_update')
]
