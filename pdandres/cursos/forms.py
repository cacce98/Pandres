from django import forms
from .models import ComCont

class ComContForm(forms.ModelForm):
    class Meta:
        model = ComCont
        fields = ['usuario', 'mensaje']