from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=True)
