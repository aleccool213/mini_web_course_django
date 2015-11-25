from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from api.serializers import purchases
from storeapp.models import Purchase


class PurchaseListCreateView(ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = purchases.PurchaseListCreateSerializer


class PurchaseUpdateView(RetrieveUpdateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = purchases.PurchaseUpdateSerializer
