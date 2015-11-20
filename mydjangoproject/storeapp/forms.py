from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Purchase


class PurchaseCreateForm(CreateView):
    template_name = "add.html"
    model = Purchase
    fields = ['name', 'price']
    success_url = '/product'
