from django.shortcuts import render, render_to_response
from django.template import RequestContext
from blog.models import *

menu_items = [
		('/about/', 'About'),
		('/admission/', 'Admission'),
		('/achievements/', 'Achievements'),
		('/activities/', 'Activities'),
		('/people/', 'People'),
		('/courses/', 'Courses'),
		('/contact-us/', 'Contact Us')
	]


def achievements(request):
    global menu_items
    articles = Article.objects.filter(category='ACH').order_by('-date')
    return render(request, "timeline.html", 
        {"activepage": "Achievements", "menu": menu_items, "articles": articles})

def activities(request):
    global menu_items
    articles = Article.objects.filter(category='ACT').order_by('-date')
    return render(request, "timeline.html", 
        {"activepage": "Activities", "menu": menu_items, "articles": articles})