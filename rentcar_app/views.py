from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from rentcar_app.models import Car, Location


class IndexView(View):
    def get(self, request):
        return render(request, "index.html")


class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'


class CarDetailsView(DetailView):
    model = Car
    template_name = 'car_details.html'
    # def get(self, request, id):
    #     car = Car.objects.get(id=id)
    #     return render(request, "car_details.html", {"car": car})


class CarAddCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['rentcar_app.add_car']
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('car_list')
    template_name = 'form.html'


class CarUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['rentcar_app.change_car']
    model = Car
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('car_list')


class CarDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['rentcar_app.delete_car']
    model = Car
    template_name = 'form.html'
    success_url = reverse_lazy('car_list')


class AddLocationView(PermissionRequiredMixin, CreateView):
    permission_required = ['rentcar_app.add_location']
    model = Location
    fields = '__all__'
    success_url = reverse_lazy('index')
    template_name = 'form.html'
