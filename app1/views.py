from django.forms import modelform_factory, modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from faker.generator import random

from django.contrib.auth.mixins import LoginRequiredMixin

from app1.models import (
    Pizza,
    Topping, Order, PizzaOrder, PizzaOrderTops,
)

from app1.forms import (
    ToppingForm,
)

class PizzaView(View):
    template_name = 'app1/pizza_view.html'

    def get(self, request, *args, **kwargs):
        is_logged_in = request.user.is_authenticated
        pizzas = Pizza.objects.all()
        ctx = {
            'pizzas': pizzas,
            'is_logged_in': is_logged_in,
        }
        return render(request, self.template_name, ctx)


class PizzaDetailsView(View):
    template_name = 'app1/pizza_details_view.html'

    def get(self, request, *args, **kwargs):
        pizza_id = kwargs['pk']
        pizza = get_object_or_404(Pizza, pk=pizza_id)

        ctx = {
            'pizza': pizza,
        }
        return render(request, self.template_name, ctx)


class ToppingView(View):
    template_name = 'app1/topping_view.html'

    def get(self, request, *args, **kwargs):
        toppings = Topping.objects.all()
        ctx = {
            'toppings': toppings,
        }
        return render(request, self.template_name, ctx)


class PizzaToppingsView(LoginRequiredMixin, View):
    template_name = 'app1/pizza_topping_view.html'
    login_url = reverse_lazy('accounts:login')

    def get(self, request, *args, **kwargs):
        form = ToppingForm()
        ToppingFormSet = modelformset_factory(Topping, ToppingForm, extra=0)
        formset = ToppingFormSet(queryset=Topping.objects.all())
        message = None
        pizza_id = kwargs['pk']
        pizza = get_object_or_404(Pizza, pk=pizza_id)
        context = {
            'form': form,
            'pizza': pizza,
            'formset': formset,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ToppingForm(request.POST)
        pizza_id = kwargs['pk']
        pizza = get_object_or_404(Pizza, pk=pizza_id)
        ToppingFormSet = modelformset_factory(Topping, ToppingForm, extra=0)
        formset = ToppingFormSet(request.POST, queryset=Topping.objects.all())
        user = request.user
        order_price = pizza.price
        if formset.is_valid():
            for topping in formset.cleaned_data:  # topping to pojedynczy slownik, ktory sie zmienia co kazde przejscie
                if topping['number'] != None:
                    order_price += topping['price'] * topping['number']
            create_order = Order.objects.create(user=user, order_price=order_price)
            pizza_order = PizzaOrder.objects.create(pizza=pizza, order=create_order, amount=1)

            for topping in formset.cleaned_data:
                if topping['number'] != None:
                    topping_id = topping['id']
                    PizzaOrderTops.objects.create(pizza_order=pizza_order, pizza_top=topping_id,
                                                  amount=topping['number'])

        else:
            context = {
                'pizza': pizza,
                'formset': formset,
            }
            return render(request, self.template_name, context)
        return redirect('pizza-order', pk=create_order.pk)


class OrderView(View):
    template_name = 'app1/pizzaorder_view.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        order_id = kwargs['pk']
        order = get_object_or_404(Order, pk=order_id)
        pizzas = order.pizzas.all()
        pizza_orders = PizzaOrder.objects.filter(order__pk=order_id)
        context = {
            'pizza_orders': pizza_orders,

        }

        return render(request, self.template_name, context)
