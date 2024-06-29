from django import forms
from .models import *

class EventManagement(forms.ModelForm):
    class Meta:
        model = Event
        fields= ['name', 'begin', 'location', 'desc', 'creator']