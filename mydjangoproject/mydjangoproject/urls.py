from django.conf.urls import include, url
from django.contrib import admin

from storeapp.views import ProductIndexView
from storeapp.forms import PurchaseCreateForm


urlpatterns = [
    # Examples:
    # url(r'^$', 'mydjangoproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^product/add', PurchaseCreateForm.as_view()),
    url(r'^product/', ProductIndexView.as_view()),

]
