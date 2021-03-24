import pytest

# from django.test import Client
from app1.models import Pizza, Topping
from django.core.management import call_command


# @pytest.fixture
# def client():
#     return Client()

@pytest.fixture
def addPizza():
    Pizza.objects.create(name="Margarita", price=19, description='sos pomidorowy, mozarella')
    Pizza.objects.create(name="Funghi", price=24, description='sos pomidorowy, mozarella, pieczarki')
    Pizza.objects.create(name="Cotto", price=25, description='sos pomidorowy, mozarella, szynka cotto')

@pytest.fixture
def addTopping():
    Topping.objects.create(name="Oliwki", price=4.99)
    Topping.objects.create(name="Kukurydza", price=1.99)
    Topping.objects.create(name="Chilli", price=2.99)






# def pizza():
#     return Pizza.objects.create(name="Margarita", price=19, description='sos pomidorowy, mozarella')