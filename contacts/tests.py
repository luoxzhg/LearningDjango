from django.shortcuts import reverse
from django.test import TestCase
from django.test.client import RequestFactory

from .models import Contact
from .views import ListContactView, CreateContactView
from .forms import ContactForm

# Create your tests here.
class ContactTests(TestCase):
    """ Contact model tests."""
    def test_str(self):
        contact = Contact(first='John', last='Smith')
        self.assertEquals(str(contact), 'John Smith')

class ContactListViewTests(TestCase):
    "Contact list view tests."
    
    def test_contacts_in_the_context(self):
        def _getResponse():
            return self.client.get(reverse('contacts:contacts-list'))

        response = _getResponse()
        self.assertEquals(
            list(response.context_data['object_list']), []
        )

        Contact.objects.create(first='foo', last='bar')
        response = _getResponse()
        self.assertEquals(
            response.context_data['object_list'].count(), 1
        )


    def test_contacts_in_the_context_request_factory(self):
        factory = RequestFactory()
        request = factory.get(reverse('contacts:contacts-list'))
        response = ListContactView.as_view()(request)
        self.assertEquals(
            list(response.context_data['object_list']), []
        )

        Contact.objects.create(first='foo', last='bar')
        response = ListContactView.as_view()(request)
        self.assertEquals(
            response.context_data['object_list'].count(), 1
        )

class ContactFormTests(TestCase):
    def test_mismatch_email_is_invalid(self):
        data={'first': 'Foo',
              'last': 'Bar',
              'email':'foo@example.com',
              'confirm_email': 'bar@example.com'
        }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())

    def test_same_email_is_valid(self):
        data={'first': 'Foo',
              'last': 'Bar',
              'email':'foo@example.com',
              'confirm_email': 'foo@example.com'
        }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())
        
