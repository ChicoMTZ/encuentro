from django.conf.urls import url, include
from django.contrib import admin
from web1.views import *


extra_patterns = [

    url(r'^accounts/', include('registration.backends.hmac.urls')),

    ]

urlpatterns = extra_patterns + [

    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^accounts/new_profile/$', createProfile.as_view(), name='New_Profile'),
]