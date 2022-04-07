import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_index():
    client = Client()
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_contact():
    client = Client()
    url = reverse('contact')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_car_list():
    client = Client()
    url = reverse('car_list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_car_details_not_login(cars):
    car = cars[0]
    client = Client()
    url = reverse('car_details', args=(car.id,))
    response = client.get(url)
    assert response.status_code == 302
    url = reverse('login')
    assert response.url.startswith(url)


@pytest.mark.django_db
def test_car_details_login(user, cars):
    car = cars[0]
    client = Client()
    url = reverse('car_details', args=(car.id,))
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_add_car_not_login(brand, type):
    client = Client()
    url = reverse('car_add')
    data = {
        'brand': brand.id,
        'model': 'test',
        'type': type.id,
        'power': 150,
        'engine': 2.0,
        'year': 2004,
        'seats': 5,
        'gears': 1,
        'fuel': 1,
        'price_per_day': 50,
        'quantity': 1,
    }
    response = client.post(url, data)
    assert response.status_code == 302
    url = reverse('login')
    assert response.url.startswith(url)


@pytest.mark.django_db
def test_add_car_as_superuser(superuser, brand, type):
    client = Client()
    client.force_login(superuser)
    url = reverse('car_add')
    data = {
        'brand': brand.id,
        'model': 'test',
        'type': type.id,
        'power': 150,
        'engine': 2.0,
        'year': 2004,
        'seats': 5,
        'gears': 1,
        'fuel': 1,
        'price_per_day': 50,
        'quantity': 1,
    }
    response = client.post(url, data)
    assert response.status_code == 302


@pytest.mark.django_db
def test_add_car_as_user(user, brand, type):
    client = Client()
    client.force_login(user)
    url = reverse('car_add')
    data = {
        'brand': brand.id,
        'model': 'test',
        'type': type.id,
        'power': 150,
        'engine': 2.0,
        'year': 2004,
        'seats': 5,
        'gears': 1,
        'fuel': 1,
        'price_per_day': 50,
        'quantity': 1,
    }
    response = client.post(url, data)
    assert response.status_code == 403


@pytest.mark.django_db
def test_car_update_view_as_superuser(superuser, cars, type, brand):
    car = cars[0]
    client = Client()
    client.force_login(superuser)
    url = reverse('car_update', args=(car.id,))
    data = {
        'brand': brand.id,
        'model': 'test',
        'type': type.id,
        'power': 150,
        'engine': 2.0,
        'year': 2005,
        'seats': 3,
        'gears': 1,
        'fuel': 1,
        'price_per_day': 60,
        'quantity': 1,
    }
    response = client.post(url, data)
    assert response.status_code == 302


@pytest.mark.django_db
def test_car_update_view_as_user(user, cars, type, brand):
    car = cars[0]
    client = Client()
    client.force_login(user)
    url = reverse('car_update', args=(car.id,))
    data = {
        'brand': brand.id,
        'model': 'test',
        'type': type.id,
        'power': 150,
        'engine': 2.0,
        'year': 2005,
        'seats': 3,
        'gears': 1,
        'fuel': 1,
        'price_per_day': 60,
        'quantity': 1,
    }
    response = client.post(url, data)
    assert response.status_code == 403


@pytest.mark.django_db
def test_car_delete_as_superuser(superuser, cars, type, brand):
    car = cars[0]
    client = Client()
    client.force_login(superuser)
    url = reverse('car_delete', args=(car.id,))
    response = client.post(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_car_delete_as_user(user, cars, type, brand):
    car = cars[0]
    client = Client()
    client.force_login(user)
    url = reverse('car_delete', args=(car.id,))
    response = client.post(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_add_location_login_as_superuser(superuser):
    client = Client()
    client.force_login(superuser)
    url = reverse('location_add')
    data = {
        'name': 'Poznań',
    }
    response = client.post(url, data)
    assert response.status_code == 302


@pytest.mark.django_db
def test_add_location_login_as_user(user):
    client = Client()
    client.force_login(user)
    url = reverse('location_add')
    data = {
        'name': 'Poznań',
    }
    response = client.post(url, data)
    assert response.status_code == 403


@pytest.mark.django_db
def test_add_rent_login(user, location, cars):
    car = cars[0]
    client = Client()
    client.force_login(user)
    url = reverse('car_rent')
    data = {
        'car': car.id,
        'start_date': '2022-05-01',
        'end_date': '2022-05-02',
        'location': location.id
    }
    response = client.post(url, data)
    assert response.status_code == 302


@pytest.mark.django_db
def test_rent_list_not_login():
    client = Client()
    url = reverse('rent_list')
    response = client.get(url)
    assert response.status_code == 302
    url = reverse('login')
    assert response.url.startswith(url)


@pytest.mark.django_db
def test_rent_list_login(user):
    client = Client()
    client.force_login(user)
    url = reverse('rent_list')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == 0


@pytest.mark.django_db
def test_rent_list_with_rents_login(user, rents):
    client = Client()
    client.force_login(user)
    url = reverse('rent_list')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(rents)
    for rent in rents:
        assert rent in response.context['object_list']


@pytest.mark.django_db
def test_add_rent_not_login(location, cars):
    car = cars[0]
    client = Client()
    url = reverse('car_rent')
    data = {
        'car': car.id,
        'start_date': '2022-05-01',
        'end_date': '2022-05-02',
        'location': location.id
    }
    response = client.post(url, data)
    assert response.status_code == 302
    url = reverse('login')
    assert response.url.startswith(url)


@pytest.mark.django_db
def test_rent_details_login(user, rents):
    rent = rents[0]
    client = Client()
    url = reverse('rent_details', args=(rent.id,))
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_rent_details_not_login(rents):
    rent = rents[0]
    client = Client()
    url = reverse('rent_details', args=(rent.id,))
    response = client.get(url)
    assert response.status_code == 302
    url = reverse('login')
    assert response.url.startswith(url)


@pytest.mark.django_db
def test_rent_edit_login(user, rents, location):
    rent = rents[0]
    client = Client()
    client.force_login(user)
    url = reverse('rent_edit', args=(rent.id,))
    data = {
        'location': location.id,
        'start_date': '2022-05-05',
        'end_date': '2022-05-08',
    }
    response = client.post(url, data)
    assert response.status_code == 302


@pytest.mark.django_db
def test_rent_edit_not_login(rents):
    rent = rents[0]
    client = Client()
    url = reverse('rent_edit', args=(rent.id,))
    response = client.get(url)
    assert response.status_code == 302
    url = reverse('login')
    assert response.url.startswith(url)


@pytest.mark.django_db
def test_rent_delete_login(user, rents):
    rent = rents[0]
    client = Client()
    client.force_login(user)
    url = reverse('rent_delete', args=(rent.id,))
    response = client.post(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_rent_delete_not_login(rents):
    rent = rents[0]
    client = Client()
    url = reverse('rent_delete', args=(rent.id,))
    response = client.post(url)
    assert response.status_code == 302
    url = reverse('login')
    assert response.url.startswith(url)
