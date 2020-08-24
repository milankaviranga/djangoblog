from django import forms
from post.models import Visiters

class VisiterEmail(forms.ModelForm):
    class Meta:
        model = Visiters
        fields = '__all__'