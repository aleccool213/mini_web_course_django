from django.conf.urls import url

from api.views.purchase_views import PurchaseListCreateView, PurchaseUpdateView


urlpatterns = [
    url(
        regex=r"^product/$",
        view=PurchaseListCreateView.as_view(),
        name="purchase_list_api"
    ),
    url(
        regex=r"^product/(?P<pk>\d+)/$",
        view=PurchaseUpdateView.as_view(),
        name="purchase_list_api"
    )
]
