from django.core.management.base import BaseCommand
from app1.models import Pizza, Topping, PizzaTops
from app1.management.commands._private import create_Topping, create_Pizza


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        create_Topping()
        create_Pizza()
        self.stdout.write(self.style.SUCCESS("wygenerowane w bazie danych"))