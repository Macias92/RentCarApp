import pytest
from django.contrib.auth.models import User, Group


@pytest.fixture
def group():
    return Group.objects.create(name="client")