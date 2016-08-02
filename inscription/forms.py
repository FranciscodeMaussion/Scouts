from django import forms
from django.forms import ModelForm
from inscription.models import Member

class Members(ModelForm):
    tutors = forms.CharField(required=False)
    pic = forms.FileField(required=False)
    formation = forms.CharField(required=False)
    class Meta:
        model = Member
        fields = ('scout','name','lastname', 'sex','dni','birthday','phone','adress','tutor','section','stage','pic','email','formation')
