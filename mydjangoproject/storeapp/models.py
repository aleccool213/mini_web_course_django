from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Purchase(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=10)
    manager = models.ForeignKey(User, null=True)


class Item(models.Model):
    purchases = models.ManyToManyField(Purchase)
