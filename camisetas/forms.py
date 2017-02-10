# -*- coding: utf-8 -*-
from camisetas.models import *
from django import forms


class TshirtForm(forms.ModelForm):
    class Meta:
        model = Tshirt
        fields = ['size', 'amount']
