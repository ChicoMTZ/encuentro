from registration.forms import *
from actividades.models import *


class InsertTopic(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ['name', 'description']


class InsertSpeech(forms.ModelForm):

    class Meta:
        model = Speech
        fields = ['title', 'description', 'notes', 'speaker_information','audience', 'skill_level',
                  'speech_type',]
