from rest_framework import serializers

from storeapp.models import Purchase


class PurchaseListCreateSerializer(serializers.ModelSerializer):

    manager_username = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        source='manager'
    )

    class Meta:
        model = Purchase
        fields = ['id', 'name', 'price', 'manager_username']


class PurchaseUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = ['name', 'price']

    def validate_price(self, value):
        if value > 100:
            raise serializers.ValidationError('Too high of a price.')
        return value
