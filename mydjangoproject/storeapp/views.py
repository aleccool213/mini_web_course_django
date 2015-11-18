# Create your views here.
from django.views.generic import TemplateView

from storeapp.models import Purchase


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['purchases'] = Purchase.objects.all()
        return context
