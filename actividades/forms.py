from registration.forms import *
from actividades.models import *
from web1.models import Profile, Eventos


class InsertTopic(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ['name', 'description']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['name', 'LastName', 'country','gender', 'identification',]


class EventoForm(forms.ModelForm):

    class Meta:
        model = Eventos
        fields = ['event_name', 'date_start', 'date_end','country', 'places',]


class InsertSpeech(forms.ModelForm):

    class Meta:
        model = Speech
        fields = ['title', 'description', 'notes', 'speaker_information','audience', 'skill_level',
                  'speech_type',]
