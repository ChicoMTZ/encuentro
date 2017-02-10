# -*- coding: utf-8 -*-
from django.conf.urls import url
from faq.views import Faq

urlpatterns = [
    url(r'^$', Faq.as_view(), name='faq'),
    ]

