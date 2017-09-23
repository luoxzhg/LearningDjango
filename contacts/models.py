from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Contact(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    email = models.EmailField(blank=True)

    def __str__(self):
        return ' '.join([self.first, self.last])

    def get_absolute_url(self):
        return reverse('contacts:contacts-view', kwargs={'pk':self.id})


class Address(models.Model):
    contact = models.ForeignKey(Contact)
    address_type = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    post_code = models.CharField(max_length=20)

    class Meta:
        unique_together = ('contact', 'address')
