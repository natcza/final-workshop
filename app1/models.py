from django.db import models
from django.conf import settings

# PIZZA_SIZES = (
#     (1, "small"),
#     (2, "medium"),
#     (3, "big"),
# )

TOP_AMOUNT = (
    ('h', 'half'),
    ('n', 'normal'),
    ('d', 'double'),
)


# class User(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255)
#     password = models.CharField(max_length=50)
#     address = models.ForeignKey("Address", related_name='users', on_delete=models.CASCADE, null=True)


# class Address(models.Model):
#     street = models.CharField(max_length=255)
#     postal_code = models.CharField(max_length=12)
#     city = models.CharField(max_length=255)


class Topping(models.Model):
    name = models.CharField(max_length=255, blank=True, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=255)
    # size = models.IntegerField(choices=PIZZA_SIZES, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    toppings = models.ManyToManyField(Topping, through="PizzaTops")


class PizzaTops(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)
    amount = models.CharField(max_length=1, choices=TOP_AMOUNT, default='n')


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_price = models.DecimalField(max_digits=6, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    # size = models.IntegerField(choices=PIZZA_SIZES, blank=True)
    pizzas = models.ManyToManyField(Pizza, through="PizzaOrder", related_name='orders')
    note = models.TextField(blank=True)


class PizzaOrder(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(PizzaTops, through='PizzaOrderTops')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()


class PizzaOrderTops(models.Model):
    pizza_order = models.ForeignKey(PizzaOrder, on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)
    amount = models.IntegerField()