from django.conf.urls import url
from django.contrib import admin
from web1.views import *


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^crear/', crear, name='index_site'),
]