from django.db import models

# Create your models here.


class Purchase(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=50)


class Item(models.Model):
    purchases = models.ManyToManyField(Purchase)
