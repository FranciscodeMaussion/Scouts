from django import forms
from django.forms import ModelForm
from inscription.models import Affiliate, Scout, Adult

class ScoutForm(ModelForm):
    class Meta:
        model = Scout
        fields = ('name', 'gender', 'dni', 'birthday', 'phone', 'adress', 'tutor', 'section', 'stage', 'picture', 'email')

class AdultForm(ModelForm):
    class Meta:
        model = Adult
        fields = ('name', 'gender', 'dni', 'birthday', 'phone', 'adress', 'formation', 'email')
