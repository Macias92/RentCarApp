from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView

from rentcar_app.models import Car


class IndexView(View):
    def get(self, request):
        return render(request, "index.html")


class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'


class CarAddCreateView(CreateView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('car_list')
    template_name = 'form.html'


class CarUpdateView(UpdateView):
    model = Car
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('car_list')
