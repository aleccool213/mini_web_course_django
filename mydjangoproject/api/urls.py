from django.conf.urls import url

from api.views.purchase_views import PurchaseListView


urlpatterns = [
    url(
        regex=r"^product/$",
        view=PurchaseListView.as_view(),
        name="purchase_list_api"
    )
]
