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


@pytest.mark.django_db
def test_profile_details_login(user, profile):
    client = Client()
    client.force_login(user)
    url = reverse('profile_details', args=(user.id,))
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_details_not_login(profile):
    client = Client()
    url = reverse('profile_details', args=(profile.id,))
    response = client.get(url)
    assert response.status_code == 302
    url = reverse('login')
    assert response.url.startswith(url)


@pytest.mark.django_db
def test_update_group_permission_not_login(group):
    client = Client()
    url = reverse('update_group_permissions', args=(group.id,))
    response = client.get(url)
    assert response.status_code == 302
    url = reverse('login')
    assert response.url.startswith(url)


@pytest.mark.django_db
def test_update_group_permission_as_user(user, group):
    client = Client()
    client.force_login(user)
    url = reverse('update_group_permissions', args=(group.id,))
    response = client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_update_group_permission_as_superuser(superuser, group):
    client = Client()
    client.force_login(superuser)
    url = reverse('update_group_permissions', args=(group.id,))
    response = client.get(url)
    assert response.status_code == 200
