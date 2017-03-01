from django.conf.urls import url
from actividades.views import *

urlpatterns = [

    # Urls domains
    url(r'^$', foro.as_view(), name='Forum'),
    url(r'^(?P<slug>[\w-]+)/insert_speech/$', insert_speech.as_view(), name='Insert_Speech'),
    url(r'^(?P<slug>[\w-]+)/$', foro_topic.as_view(), name='Forum_Topic'),
    url(r'^(?P<slug>[\w-]+)/(?P<slug1>[\w-]+)/$', foro_detail.as_view(), name='Forum_Detail'),
    url(r'^filter/type/(?P<slug>[\w-]+)/$', foro_types.as_view(), name='Forum_Types'),
    url(r'^(?P<speech_id>[0-9]+)/nuevo_recurso$', subirRecurso.as_view(), name='subir_recurso'),

]