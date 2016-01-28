# Create your views here.
from django.views.generic import ListView

from storeapp.models import Purchase


class ProductIndexView(ListView):
    template_name = "index.html"
    model = Purchase
