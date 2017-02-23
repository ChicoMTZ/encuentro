from django.conf.urls import url, include
from django.contrib import admin
from web1.views import *
from web1.vistas.User import *
from actividades.views import *


extra_patterns = [

    url(r'^accounts/', include('registration.backends.hmac.urls')),

    ]


domains_patterns = [

    # Urls domains
    url(r'^activity/$', foro.as_view(), name='Forum'),
    url(r'^activity/(?P<slug>[\w-]+)/insert_speech/$', insert_speech.as_view(), name='Insert_Speech'),
    url(r'^activity/(?P<slug>[\w-]+)/$', foro_topic.as_view(), name='Forum_Topic'),
    url(r'^activity/(?P<slug>[\w-]+)/(?P<slug1>[\w-]+)/$', foro_detail.as_view(), name='Forum_Detail'),
    url(r'^activity/filter/type/(?P<slug>[\w-]+)/$', foro_types.as_view(), name='Forum_Types'),
    url(r'^activity/(?P<speech_id>[0-9]+)/nuevo_recurso$', subirRecurso.as_view(), name='subir_recurso'),

]
user_patterns = [

    url(r'^accounts/view_profile/(?P<pk>[\w-]+)/$', view_profile.as_view(), name='View_Profile'),
    url(r'^accounts/new_user/$', createUser.as_view(), name='New_User'),
    url(r'^accounts/completar_registro/(?P<next>[\S]*)$', completarRegistro, name='completar_registro'),
    url(r'^accounts/salir$', salir, name='salir'),

]

urlpatterns = domains_patterns + user_patterns + extra_patterns + [

    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),

]

