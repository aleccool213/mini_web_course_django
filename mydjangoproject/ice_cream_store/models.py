from django.db import models

# Create your models here.


class Purchase(models.Model):
    price = models.IntegerField()


class Item(models.Model):
    name = models.CharField(max_length=100)
