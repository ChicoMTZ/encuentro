from registration.forms import *
from web1.models import Profile


class ProfileForm(RegistrationForm):
    name = forms.CharField(label='Name', required=True, )
    last_name = forms.CharField(label='Last name', required=True)
    event_url = forms.CharField(label='Event Name', required=True)
    email = RegistrationFormUniqueEmail()

