from django.conf.urls import url
from becas.views import becas


urlpatterns = [
    url(r'^$', becas.as_view(), name='becas'),
]