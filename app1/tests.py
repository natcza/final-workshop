# from django.test import TestCase
import pytest
from django.urls import reverse

from app1.models import Pizza


# Create your tests here.
# sprawdzenie status code200
# sprawdzenie ile jest rekordow w bazie danych

@pytest.mark.django_db
def test_pizza_list_view(client, addPizza):
    response = client.get('/pizza/')
    assert response.status_code == 200
    assert len(response.context['pizzas']) == 3
    assert response.context['is_logged_in'] == False


# Test class PizzaDetailsView(View):
@pytest.mark.django_db
def test_pizza_detail_view_get(client):
    pizza = Pizza.objects.create(name="Margarita", price=19, description='sos pomidorowy, mozarella')
    url = reverse(
        'pizza-details', kwargs={'pk': pizza.pk}
    )
    response = client.get(url)
    raise
    assert response.status_code == 200
    assert response.context['pizza'] == pizza

# def test_login(client, funkcjatworzacaUser):
#     response = client.login(unsername='username', password='password')
#     code == 200
#
#     response = client.login(unsername='username', password='zle haslo')
#     code == 401


# i = 0
# while True:
#     i += 1
#     assert i < 4, "Za duza liczba"
#     print("i = %s, ide dalej." % i)
#
#
# def add(a, b):
#     return a + b
#
#
# def test_add():
#     assert add(2, 2) == 4
#
#
# test_add()


# def test_to_fail():
#     assert True
#
#
# def test_to_be_ok():
#     assert 2 + 2 == 4
