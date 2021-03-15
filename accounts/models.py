from django.db import models

from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.


class Address(models.Model):
    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=12)
    city = models.CharField(max_length=255)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)