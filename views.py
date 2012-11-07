from django.http import HttpResponseForbidden, HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from blog.models import Article
from django.core.mail import send_mail



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

