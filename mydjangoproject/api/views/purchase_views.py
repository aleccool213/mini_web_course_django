from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from api.serializers import purchases
from storeapp.models import Purchase


class PurchaseListCreateView(ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = purchases.PurchaseListCreateSerializer

    def perform_create(self, serializer):
        '''Set purchase manager to the current user.'''
        if not self.request.user.is_anonymous():
            serializer = serializer.save(manager=self.request.user)
        return serializer.save()


class PurchaseUpdateView(RetrieveUpdateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = purchases.PurchaseUpdateSerializer
