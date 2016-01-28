# Create your views here.
from django.views.generic import ListView

from ice_cream_store.models import Receipt


class ProductIndexView(ListView):
    template_name = "index.html"
    model = Receipt
