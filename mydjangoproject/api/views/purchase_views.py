from rest_framework.generics import ListCreateAPIView

from api.serializers import purchases
from storeapp.models import Purchase


class PurchaseListCreateView(ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = purchases.PurchaseListSerializer
