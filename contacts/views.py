from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (
    DetailView,ListView,
    CreateView, UpdateView, DeleteView
)

from .models import Contact
from .forms import ContactForm, ContactAddressFormSet

# Create your views here.
class DetailContactView(DetailView):
    model = Contact
    template_name = 'contacts/contact.html'

class ListContactView(ListView):
    model = Contact
    template_name = 'contacts/contact_list.html'


class CreateContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/edit_contact.html'


    def get_success_url(self):
        return reverse('contacts:contacts-list')


class UpdateContactView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/edit_contact.html'

    def get_success_url(self):
        return reverse('contacts:contacts-list')

class DeleteContactView(DeleteView):
    model = Contact
    template_name='contacts/delete_contact.html'

    def get_success_url(self):
        return reverse('contacts:contacts-list')

class EditContactAddressView(UpdateView):
    model = Contact
    template_name = 'contacts/edit_addresses.html'
    form_class = ContactAddressFormSet

    def get_success_url(self):
        # redirect to the Contact
        return self.object.get_absolute_url()
