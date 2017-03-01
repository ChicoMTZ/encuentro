from django.conf.urls import url, include
from web1.views import *
from web1.vistas.User import *
from django.conf.urls.static import static
from web1.admin import admin_site

from web1.admin import admin_site

extra_patterns = [

    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^tshirts/', include('camisetas.urls', namespace='tshirts')),
    url(r'^faq/', include('faq.urls', namespace='faq')),
    url(r'^activity/', include('actividades.urls', namespace='activity')),
    url(r'^becas/', include('becas.urls', namespace='becas')),
    ]


user_patterns = [

    url(r'^accounts/view_profile/(?P<pk>[\w-]+)/$', view_profile.as_view(), name='View_Profile'),
    url(r'^accounts/new_user/$', createUser.as_view(), name='New_User'),
    url(r'^accounts/new_profile/$', createProfile.as_view(), name='New_Profile'),
    url(r'^accounts/salir/$', salir, name='salir'),
    url(r'^accounts/edit_profile/(?P<pk>[0-9]+)$', ProfileUpdateView.as_view(), name='edit_profile'),
    url(r'^accounts/create_event/(?P<pk>[0-9]+)$', createEvent.as_view(), name='Create_Event'),

]

urlpatterns = user_patterns + extra_patterns + [

    url(r'^admin/', admin_site.urls),
    url(r'^$', index, name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
