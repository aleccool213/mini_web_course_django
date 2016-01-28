from django.db import models

# Create your models here.


class Receipt(models.Model):
    price = models.IntegerField()


class Item(models.Model):
    name = models.CharField(max_length=100)
    receipts = models.ManyToManyField(Receipt)
