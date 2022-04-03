import pytest
from django.contrib.auth.models import User

from rentcar_app.models import Car, Brand, Type


@pytest.fixture
def user():
    return User.objects.create_user(username="1test", password="1test")


@pytest.fixture
def superuser():
    return User.objects.create_superuser(username='test', password='testt')


@pytest.fixture
def brand():
    return Brand.objects.create(name=1)


@pytest.fixture
def type():
    return Type.objects.create(name=1)


@pytest.fixture
def cars(brand, type):
    lst = []
    for i in range(5):
        x = Car.objects.create(brand=brand,
                               model='i',
                               type=type,
                               power=i,
                               engine=i,
                               year=i,
                               seats=i,
                               gears=0,
                               fuel=0,
                               price_per_day=i,
                               quantity=1)
        lst.append(x)
    return lst
