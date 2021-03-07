from random import choice, randint
from sys import stdout
# from faker import Factory
from app1.models import Pizza, Topping


def create_Topping():
    Topping.objects.create(name="Oliwki", price=4.99)
    Topping.objects.create(name="Kukurydza", price=1.99)
    Topping.objects.create(name="Chilli", price=2.99)
    Topping.objects.create(name="Rukola", price=3.99)
    Topping.objects.create(name="Karczochy", price=5.99)
    Topping.objects.create(name="Jalapeno", price=2.99)
    Topping.objects.create(name="Gorgonzola", price=4.99)
    Topping.objects.create(name="Cheddar", price=3.99)
    Topping.objects.create(name="Grana Padano", price=4.99)
    Topping.objects.create(name="Pomidorki koktailowe", price=2.99)
    Topping.objects.create(name="Mascarpone", price=4.99)
    Topping.objects.create(name="Szpinak z pesto", price=3.99)
    Topping.objects.create(name="Czosnek marynowany", price=2.99)


def create_Pizza():
    Pizza.objects.create(name="Margarita", size=1, price=19)
    Pizza.objects.create(name="Funghi", size=1, price=24)
    Pizza.objects.create(name="Cottp", size=1, price=25)
    Pizza.objects.create(name="Fec", size=1, price=26)
    Pizza.objects.create(name="Diavola", size=1, price=27)
    Pizza.objects.create(name="Vege", size=1, price=28)
