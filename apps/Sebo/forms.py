from django import forms
from .models import *

class formDisco(forms.ModelForm):
    class Meta:
        model = Disco
        fields = '__all__'