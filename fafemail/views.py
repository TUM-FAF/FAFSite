from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import send_mail
from fafemail.models import *
from django.views.decorators.csrf import csrf_exempt
from forms import ContactForm
from datetime import datetime
from shared import get_menu_items

menu_items = get_menu_items()

def save_in_db(_name, _email, _message):
	_timestamp = datetime.now()
	e = Email(timestamp = _timestamp,
			name = _name,
			email = _email,
			message = _message)
	e.save()


@csrf_exempt
def contact_us(request):
    global menu_items
    response = ''
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
                send_mail('[FAF]Contact us', messageBody, email, ['ana.balica@gmail.com'], fail_silently=False)
                # response = '<span>*</span> Thank you. We will consider your message as soon as possible and contact you.'
            except:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/contact-us/thanks/')
    # else:
    #     form = ContactForm()
    return render(request, "contact-us.html", 
        {"activepage": "Contact Us", "menu": menu_items, "form": form})


def thanks(request):
    global menu_items
    form = ContactForm()
    response = '<span>*</span> Thank you. We will consider your message as soon as possible and contact you.'
    return render(request, "contact-us.html",
        {"activepage": "Contact Us", "menu": menu_items, "form": form,"response": response})

def sorry(request):
    global menu_items
    form = ContactForm()
    response = "Sorry, your form has not been submitted."
    return render(request, "contact-us.html",
        {"activepage": "Contact Us", "menu": menu_items, "form": form,"response": response})

