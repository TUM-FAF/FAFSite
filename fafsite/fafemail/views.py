from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import ContactForm


def save_in_db(_name, _email, _message):
    _timestamp = datetime.now()
    e = Email(timestamp=_timestamp,
              name=_name,
              email=_email,
              message=_message)
    e.save()


@csrf_exempt
def contact_us(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['surname'] != '':
                return HttpResponseRedirect('/contact-us/sorry/')
            name = cd['name']
            email = cd['email']
            message = cd['message']
            save_in_db(name, email, message)
            messageBody = '\n\nFROM: ' + email + '\n\nName: ' + name + '\n\nMessage: ' + message
            try:
                send_mail('[FAF]Contact us', messageBody, email,
                          ['ana.balica@gmail.com'], fail_silently=False)
            except:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/contact-us/thanks/')
    return render(request, "contact-us.html",
                  {"activepage": "Contact Us",
                   "form": form})


def thanks(request):
    form = ContactForm()
    response = '<span>*</span> Thank you. We will consider your message as soon as possible and contact you.'
    return render(request, "contact-us.html",
                  {"activepage": "Contact Us", "form": form,
                   "response": response})


def sorry(request):
    form = ContactForm()
    response = "Sorry, your form has not been submitted."
    return render(request, "contact-us.html",
                  {"activepage": "Contact us", "form": form,
                   "response": response})
