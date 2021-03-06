from django.core.management.base import BaseCommand
from app1.models import Pizza, Topping


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Pizza.objects.create(name="Marinara", size=2, price=26.99)