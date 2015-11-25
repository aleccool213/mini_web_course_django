from rest_framework import serializers

from storeapp.models import Purchase


class PurchaseListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = ['name', 'price']
