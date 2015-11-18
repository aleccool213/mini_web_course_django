from django.conf.urls import include, url
from django.contrib import admin

from storeapp.views import ProductIndexView


urlpatterns = [
    # Examples:
    # url(r'^$', 'mydjangoproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', ProductIndexView.as_view())
]
