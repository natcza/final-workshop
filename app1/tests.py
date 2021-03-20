# from django.test import TestCase
import pytest


# Create your tests here.
# sprawdzenie status code200
# sprawdzenie ile jest rekordow w bazie danych

@pytest.mark.django_db
def test_pizza_list_view(client, addPizza):
    response = client.get('/pizza/')
    assert response.status_code == 200
    assert len(response.context['pizzas']) == 2
    assert response.context['is_logged_in'] == False


def test_login(client, funkcjatworzacaUser):
    response = client.login(unsername='username', password='password')
    code == 200

    response = client.login(unsername='username', password='zle haslo')
    code == 401