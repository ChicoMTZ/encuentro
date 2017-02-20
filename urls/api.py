from django.conf.urls import url
from web1.views import *

urlpatterns = [

    url(r'^home/', apis),
]