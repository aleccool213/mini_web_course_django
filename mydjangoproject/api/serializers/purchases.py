from rest_framework import serializers

from storeapp.models import Purchase


class PurchaseListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = ['name', 'price']
