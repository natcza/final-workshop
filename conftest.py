import pytest

from django.test import Client
from app1.models import Pizza
from django.core.management import call_command


@pytest.fixture
def client():
    return Client()

@pytest.fixture
def addPizza():
    Pizza.objects.create(name="Margarita", price=19, description='sos pomidorowy, mozarella')
    Pizza.objects.create(name="Margarita", price=19, description='sos pomidorowy, mozarella')


