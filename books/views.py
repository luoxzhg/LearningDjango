from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .forms import ContactForm
# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(requst.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(cd['subject'],
                      cd['message'],
                      cd.get('email', 'noreply@example.com'),
                      ['siteowner@example.com'],
                    )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm( initial={'subject': 'I love your site!'} )
    return render(request, 'contact_form.html', {'form': form})
