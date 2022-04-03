import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from rentcar_app.filters import CarFilter
from rentcar_app.forms import RentEditForm
from rentcar_app.models import Car, Location, Rent


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


def car_list(request):
    car = CarFilter(request.GET, queryset=Car.objects.all())
    return render(request, 'car_list.html', {'filter': car})


class CarDetailsView(LoginRequiredMixin, DetailView):
    model = Car
    template_name = 'car_details.html'


class CarAddCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['rentcar_app.add_car']
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('car_list')
    template_name = 'form.html'


    # def get(self,request, *args,**kwargs):
    #     super().get(self,request, *args,**kwargs)


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


class RentCarView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        cars = Car.objects.all()
        locations = Location.objects.all()
        return render(request, 'car_rent.html', context={'cars': cars, 'locations': locations})

    def post(self, request):
        cars = Car.objects.all()
        locations = Location.objects.all()
        user_id = request.user.id
        car_id = request.POST.get('car')
        location_id = request.POST.get('location')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        if Rent.objects.filter(car_id=car_id, start_date=start_date):
            return render(request, 'car_rent.html', context={'cars': cars,
                                                             'locations': locations,
                                                             'error': 'In this period of time that car is already rented. '
                                                                      'Choose other dates!'})

        if Rent.objects.filter(car_id=car_id, start_date=end_date):
            return render(request, 'car_rent.html', context={'cars': cars,
                                                             'locations': locations,
                                                             'error': 'In this period of time that car is already rented. '
                                                                      'Choose other dates!'})

        if Rent.objects.filter(car_id=car_id, end_date=start_date):
            return render(request, 'car_rent.html', context={'cars': cars,
                                                             'locations': locations,
                                                             'error': 'In this period of time that car is already rented. '
                                                                      'Choose other dates!'})
        if start_date < str(datetime.date.today()):
            return render(request, 'car_rent.html', context={'cars': cars,
                                                             'locations': locations,
                                                             'error': 'Incorrect date - date cannot be past!'})

        Rent.objects.create(car_id=car_id,
                            user_id=user_id,
                            start_date=start_date,
                            end_date=end_date,
                            location_id=location_id)
        return redirect('car_list')


class RentListView(LoginRequiredMixin, ListView):
    model = Rent
    template_name = 'rent_list.html'
    ordering = ['-pk']


class RentDetailsView(DetailView):
    def get(self, request, pk):
        rent = Rent.objects.get(pk=pk)
        price = rent.car.price_per_day
        day_start = rent.start_date
        day_end = rent.end_date
        delta = day_end - day_start
        days = delta.days
        summary = days * price
        return render(request, 'rent_details.html', context={'rent': rent,
                                                             'price': price,
                                                             'summary': summary})


class RentEditView(LoginRequiredMixin, UpdateView):
    model = Rent
    form_class = RentEditForm
    template_name = 'form.html'
    success_url = reverse_lazy('rent_list')


class RentDeleteView(LoginRequiredMixin, DeleteView):
    model = Rent
    template_name = 'form.html'
    success_url = reverse_lazy('rent_list')


def contact(request):
    return render(request, 'contact.html')

