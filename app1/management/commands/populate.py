from django.core.management.base import BaseCommand
from app1.models import Pizza, Topping, PizzaTops


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Pizza.objects.get_or_create(name="Marinara", size=2, price=26.99)
        topping_1 = Topping.objects.get_or_create(name="Oliwki", price=4.99)
        Topping.objects.get_or_create(name="Kapary", price=5.99)
        pizza1 = Pizza.objects.get(name='Marinara')
        topping1 = Topping.objects.get(name="Kapary")
        pizza1.toppings.add(topping1)
