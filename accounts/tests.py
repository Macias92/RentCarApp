import pytest
from django.test import TestCase
from django.urls import reverse
from django.test import Client
from rentcar_app.conftest import user


@pytest.mark.django_db
def test_login_get():
    client = Client()
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_post(user):
    client = Client()
    url = reverse('login')
    data = {
        'username': 'ttt',
        'password': 'test',
    }
    response = client.post(url, data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_logout_get():
    client = Client()
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_user_get():
    client = Client()
    url = reverse('create_user')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_user_post(group):
    client = Client()
    url = reverse('create_user')
    data = {
        'username': 'new_user',
        'email': 'new@user.com',
        'password': 'test',
        'first_name': 'new',
        'last_name': 'user',
    }
    response = client.post(url, data)
    assert response.status_code == 302
