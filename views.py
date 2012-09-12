from django.http import HttpResponseForbidden, HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from blog.models import Article
from django.core.mail import send_mail
from forms import ContactForm
from django.views.decorators.csrf import csrf_exempt

menu_items = [
        ('/about/', 'About'),
        ('/admission/', 'Admission'),
        ('/achievements/', 'Achievements'),
        ('/activities/', 'Activities'),
        ('/people/', 'People'),
        ('/courses/', 'Courses'),
        ('/contact-us/', 'Contact Us')
    ]

def index(request):
    global menu_items
    return render(request, "mainpage.html", 
        {"activepage": "index", "menu": menu_items})

def about(request):
    global menu_items
    return render(request, "about.html", 
        {"activepage": "About", "menu": menu_items})

def admission(request):
    global menu_items
    return render(request, "admission.html", 
        {"activepage": "Admission", "menu": menu_items})

@csrf_exempt
def contact_us(request):
    global menu_items
    response = ''
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd['name']
            email = cd['email']
            message = cd['message']
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