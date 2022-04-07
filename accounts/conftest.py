import pytest
from django.contrib.auth.models import User, Group

from rentcar_app.models import Profile


@pytest.fixture
def group():
    return Group.objects.create(name="client")


@pytest.fixture
def user():
    user = User.objects.create_user(username="11test", password="11test")
    return user


@pytest.fixture
def profile(user):
    return Profile.objects.create(user=user, tel_num=555555555,
                                  address='testowastreet',
                                  city='Testowo',
                                  zip_code='IIIII',
                                  )


@pytest.fixture
def superuser():
    return User.objects.create_superuser(username='testsuper', password='testt')


@pytest.fixture
def superuser_profile():
    return Profile.objects.create_superuser(user=superuser, tel_num=555555555,
                                            address='testowastreet',
                                            city='Testowo',
                                            zip_code='IIIII',
                                            )


@pytest.fixture
def users():
    lst = []
    for i in range(3):
        x = User.objects.create(username=i, password=i)
        lst.append(x)
    return lst
