# from django.test import TestCase
import pytest
from django.urls import reverse

from app1.models import Pizza, Topping, PizzaTops, Order, PizzaOrder, PizzaOrderTops

from django.contrib.auth.models import AnonymousUser, User
from .views import PizzaToppingsView, OrderView


# Create your tests here.
# sprawdzenie status code200
# sprawdzenie ile jest rekordow w bazie danych

@pytest.mark.django_db
def test_pizza_list_view(client, addPizza):
    response = client.get('/pizza/')
    assert response.status_code == 200
    assert len(response.context['pizzas']) == 3
    assert response.context['is_logged_in'] == False


@pytest.mark.django_db
def test_access_to_pizza_topping_view_by_anonymous_user(client, rf):
    pizza = Pizza.objects.create(name="Margarita", price=19, description='sos pomidorowy, mozarella')
    request = rf.get('/')
    request.user = AnonymousUser()
    response = PizzaToppingsView.as_view()(request, pk=pizza.pk)
    assert response.status_code == 302


@pytest.mark.django_db
def test_access_to_pizza_topping_view_by_logged_user(client, rf, admin_user):
    pizza = Pizza.objects.create(name="Margarita", price=19, description='sos pomidorowy, mozarella')
    request = rf.get('/')
    request.user = admin_user
    response = PizzaToppingsView.as_view()(request, pk=pizza.pk)
    assert response.status_code == 200


# Test class PizzaDetailsView(View):
@pytest.mark.django_db
def test_pizza_detail_view_get(client):
    pizza = Pizza.objects.create(name="Margarita", price=19, description='sos pomidorowy, mozarella')
    url = reverse(
        'pizza-details', kwargs={'pk': pizza.pk}
    )
    response = client.get(url)
    # response = client.get(url, {'pizza': pizza})
    # raise
    assert response.status_code == 200
    assert response.context['pizza'] == pizza


@pytest.mark.django_db
def test_topping_list_view(client, addTopping):
    """Test sprawdzajacy czy strona wyswietla sie poprawnie oraz czy rekordy sa poprawnie zapisane i wyswietlone """
    response = client.get('/topping/')
    assert response.status_code == 200
    # raise
    assert len(response.context['toppings']) == 3

# @pytest.mark.django_db
# def test_pizza_toppings_get_view(client):
#     pizza = Pizza.objects.create(name="Margarita", price=19, description='sos pomidorowy, mozarella')
#     url = reverse(
#         'pizza-topping', kwargs={'pk': pizza.pk}
#     )
#     response = client.get(url)
#     assert response.status_code == 200


# def test_login(client, funkcjatworzacaUser):
#     response = client.login(unsername='username', password='password')
#     code == 200
#
#     response = client.login(unsername='username', password='zle haslo')
#     code == 401




@pytest.mark.django_db
def test_access_by_anonymouse_user_to_order(rf, admin_user):
    request = rf.get('/')
    request.user = AnonymousUser()
    response = OrderView.as_view()(request, pk=5)
    assert response.status_code == 302



@pytest.mark.django_db
def test_access_by_logged_user_to_order(client, admin_user):
    client.force_login(user=admin_user)
    pizza = Pizza.objects.create(name="Margarita", price=19, description='sos pomidorowy, mozarella')
    topping = Topping.objects.create(name="Czosnek marynowany", price=2.99)
    pizza_tops = PizzaTops.objects.create(pizza=pizza, topping=topping, pizza_size=2)
    order = Order.objects.create(user=admin_user, order_price=4)
    pizza_order = PizzaOrder.objects.create(pizza=pizza, order=order, amount=1)
    pizza_order_tops = PizzaOrderTops(pizza_order=pizza_order, pizza_top=topping, amount=1)
    url = reverse(
        'pizza-order', kwargs={'pk': order.pk}
    )
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['pizza_orders']
