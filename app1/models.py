from django.db import models

PIZZA_SIZES = (
    (1, "small"),
    (2, "medium"),
    (3, "big"),
)

TOP_AMOUNT = (
    ('h', 'half'),
    ('n', 'normal'),
    ('d', 'double'),
)


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=50)
    address = models.ForeignKey("Address", related_name='users', on_delete=models.CASCADE, null=True)


class Address(models.Model):
    street = models.CharField(max_length=255)
    postal_code = models.CharField("Postal code", max_length=12)
    city = models.CharField("City", max_length=255)


class Topping(models.Model):
    name = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)


class Pizza(models.Model):
    name = models.CharField(max_length=255)
    size = models.IntegerField(choices=PIZZA_SIZES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    toppings = models.ManyToManyField(Topping, through="PizzaTops")


class PizzaTops(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)
    amount = models.CharField(max_length=1, choices=TOP_AMOUNT, default='n')


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_price = models.DecimalField(max_digits=6, decimal_places=2)
    pizza = models.ForeignKey(Pizza, related_name='orders', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    pizzas = models.ManyToManyField(Pizza, through="PizzaOrder")
    note = models.TextField(blank=True)


class PizzaOrder(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()
