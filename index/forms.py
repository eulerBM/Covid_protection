from django import forms
from index.models import *

class email(forms.ModelForm):
    class Meta:
        model = email
        fields = ['email']