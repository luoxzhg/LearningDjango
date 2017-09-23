from django import forms
from . import models

##class PersonForm(forms.Form):
##    first = forms.CharField(max_length=100)
##    middle = forms.CharField(max_length=100, required=True)
##    last  = forms.CharField(max_length=100)

class PersonForm(forms.ModelForm):
##    last = forms.CharField(initial='Smith')
    class Meta:
        model = models.Person
        fields = '__all__'
##        initial = {
##            'last': 'Smith',
##        }

class SimplePerson(PersonForm):
    class Meta(PersonForm.Meta):
        exclude = ('middle',)
