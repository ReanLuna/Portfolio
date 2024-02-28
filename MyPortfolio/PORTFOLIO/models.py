from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.FloatField()
    description = models.CharField(max_length = 100)