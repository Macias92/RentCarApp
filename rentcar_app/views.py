import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from rentcar_app.filters import CarFilter
from rentcar_app.forms import RentEditForm
from rentcar_app.models import Car, Location, Rent


class IndexView(View):  # HomePage View
    def get(self, request):
        return render(request, 'index.html')


def car_list(request):   # View displaying list of all cars from db, with filter function
    car = CarFilter(request.GET, queryset=Car.objects.all())
    return render(request, 'car_list.html', {'filter': car})


class CarDetailsView(LoginRequiredMixin, DetailView):  # View connected with car details
    model = Car
    template_name = 'car_details.html'


class CarAddCreateView(PermissionRequiredMixin, CreateView):  # View connected with adding car object to db
    permission_required = ['rentcar_app.add_car']
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('car_list')
    template_name = 'form.html'


class CarUpdateView(PermissionRequiredMixin, UpdateView):  # View connected with updating car object data
    permission_required = ['rentcar_app.change_car']
    model = Car
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('car_list')


class CarDeleteView(PermissionRequiredMixin, DeleteView):  # View connected with deleting car object from db
    permission_required = ['rentcar_app.delete_car']
    model = Car
    template_name = 'form.html'
    success_url = reverse_lazy('car_list')


class AddLocationView(PermissionRequiredMixin, CreateView):  # View connected with adding location object to db
    permission_required = ['rentcar_app.add_location']
    model = Location
    fields = '__all__'
    success_url = reverse_lazy('index')
    template_name = 'form.html'


def date_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


class RentCarView(LoginRequiredMixin, View):  # View connected with renting a car
    def get(self, request):
        user = request.user  # getting authenticated user
        cars = Car.objects.all()
        locations = Location.objects.all()
        return render(request, 'car_rent.html', context={'cars': cars, 'locations': locations})

    def post(self, request):  # Post View allows to add rent to db
        cars = Car.objects.all()
        locations = Location.objects.all()
        user_id = request.user.id
        car_id = request.POST.get('car')
        location_id = request.POST.get('location')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        rent = Rent.objects.filter(car_id=car_id)
        startdate = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        enddate = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()

        for i in rent:
            if not date_in_range(i.start_date, i.end_date, startdate):
                return render(request, 'car_rent.html', context={'cars': cars,
                                                                 'locations': locations,
                                                                 'error': 'In this period of time that car is already rented. '
                                                                      'Choose other dates!'})

            if not date_in_range(i.start_date, i.end_date, enddate):
                return render(request, 'car_rent.html', context={'cars': cars,
                                                                'locations': locations,
                                                                'error': 'In this period of time that car is already rented. '
                                                                      'Choose other dates!'})

        if start_date < str(datetime.date.today()):  # condition checking if start_date is not from the past
            return render(request, 'car_rent.html', context={'cars': cars,
                                                             'locations': locations,
                                                             'error': 'Incorrect date - date cannot be past!'})

        Rent.objects.create(car_id=car_id,
                            user_id=user_id,
                            start_date=start_date,
                            end_date=end_date,
                            location_id=location_id)
        return redirect('car_list')


class RentListView(LoginRequiredMixin, ListView):  # View connected with listing of rent cars
    model = Rent
    template_name = 'rent_list.html'
    # ordering = ['-pk']


class RentDetailsView(LoginRequiredMixin, DetailView):
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


class UserRentListView(LoginRequiredMixin, DetailView):  # View connected with list user rents
    def get(self, request):
        user = request.user
        rents = Rent.objects.filter(user_id=user.id)
        return render(request, 'user_rent_list.html', context={'rents': rents})


class RentEditView(LoginRequiredMixin, UpdateView):  # View connected with renting editing
    model = Rent
    form_class = RentEditForm
    template_name = 'form.html'
    success_url = reverse_lazy('rent_list')


class RentDeleteView(LoginRequiredMixin, DeleteView):  # View connected with delete renting
    model = Rent
    template_name = 'form.html'
    success_url = reverse_lazy('rent_list')


def contact(request):  # Contact View
    return render(request, 'contact.html')

