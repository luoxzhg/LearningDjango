from django import forms
from django.forms.models import inlineformset_factory
from django.core.exceptions import ValidationError


from .models import Contact, Address

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude=()

    confirm_email = forms.EmailField(label='Confirm email')

    def __init__(self, *args, **kwargs):
        "set initial value for confirm_email field"
        inst = kwargs.get('instance')
        if inst:
            kwargs.setdefault('initial', {})['confirm_email'] = inst.email
        super().__init__(*args, **kwargs)

    def clean(self):
        data = self.cleaned_data
        if data.get('confirm_email') != data.get('email'):
            raise ValidationError('Email address must match.')
        return data

ContactAddressFormSet = inlineformset_factory(Contact, Address, exclude=('contact',))
