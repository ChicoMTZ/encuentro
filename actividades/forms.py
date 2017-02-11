from actividades.models import *
from web1.models import Profile, Eventos
from django import forms


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


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Forum_User_Profile
        fields = ['name', 'last_name', 'gender', 'born_date', 'nationality', 'institution', 'identification',
                  'alimentary_restriction', 'health_consideration', 'snore', 'letter', 'entry_country', 'out_country',
                  'entry_port', 'out_port', 'entry_country_date', 'out_country_date', ]
        widgets = {
            'entry_country_date': forms.TextInput(attrs={'class': 'datepicker'}),
            'out_country_date': forms.TextInput(attrs={'class': 'datepicker'}),
            'born_date': forms.TextInput(attrs={'class': 'datepicker'}),
        }