from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tel_num = models.IntegerField()
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=5, blank=True)


class Brand(models.Model):
    BRANDS = (
        (0, 'Audi'),
        (1, 'BMW'),
        (2, 'Citroen'),
        (3, 'Fiat'),
        (4, 'Ford'),
        (5, 'Hyundai'),
        (6, 'Kia'),
        (7, 'Lexus'),
        (8, 'Mazda'),
        (9, 'Mercedes'),
        (10, 'Nissan'),
        (11, 'Opel'),
        (12, 'Renault'),
        (13, 'SEAT'),
        (14, 'Skoda'),
        (15, 'Tesla'),
        (16, 'Toyota'),
        (17, 'Volkswagen'),
        (18, 'Volvo'),
    )
    name = models.IntegerField(choices=BRANDS)

    def __str__(self):
        return self.get_name_display()


class Type(models.Model):
    TYPES = (
        (0, 'Convertible'),
        (1, 'Coupe'),
        (2, 'Hatchback'),
        (3, 'Minivan'),
        (4, 'Pickup Truck'),
        (5, 'Sedan'),
        (6, 'Sports Car'),
        (7, 'Station Wagon'),
        (8, 'SUV'),
    )
    name = models.IntegerField(choices=TYPES)

    def __str__(self):
        return self.get_name_display()


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    power = models.IntegerField()
    engine = models.DecimalField(max_digits=2, decimal_places=1)
    year = models.DecimalField(max_digits=4, decimal_places=0)
    seats = models.IntegerField()
    GEARS = (
        (0, 'automatic'),
        (1, 'manual'))
    gears = models.IntegerField(choices=GEARS)
    FUELS = (
        (0, 'petrol'),
        (1, 'oil'),
        (2, 'petrol+LPG'),
        (3, 'hybrid'),
        (4, 'electric'))
    fuel = models.IntegerField(choices=FUELS)
    price_per_day = models.IntegerField()

    def __str__(self):
        return f"{self.brand} {self.name}"

    def get_absolute_url(self):
        return reverse('car_update', args=(self.pk, ))


class Location(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Rent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()