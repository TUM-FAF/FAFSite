from django.shortcuts import render, render_to_response
from django.template import RequestContext
from blog.models import Article

menu_items = [
        ('/about/', 'About'),
        ('/admission/', 'Admission'),
        ('/achievements/', 'Achievements'),
        ('/activities/', 'Activities'),
        ('/people/', 'People'),
        ('#', 'Courses'),
        ('#', 'Contact Us')
    ]


def index(request):
    global menu_items
    return render(request, "mainpage.html", 
        {"page": "index", "menu": menu_items})

def about(request):
    global menu_items
    return render(request, "about.html", 
        {"page": "about", "menu": menu_items})

def courses(request):
    global menu_items
    courses = Course.objects.all()
    y = ['I','II','III','IV','V','VI','VII']
    return render(request, "courses.html", 
        {"page": "courses", "menu": menu_items, "academic": courses, "y": y})

def about_course(request):
    global menu_items
    return render(request, "about-course.html", 
        {"page": "about", "menu": menu_items})

def achievements(request):
    global menu_items
    articles = Article.objects.filter(category='ACH').order_by('-date')
    return render(request, "timeline.html", 
        {"page": "timeline", "menu": menu_items, "articles": articles})

def activities(request):
    global menu_items
    articles = Article.objects.filter(category='ACT').order_by('-date')
    return render(request, "timeline.html", 
        {"page": "timeline", "menu": menu_items, "articles": articles})

def admission(request):
    global menu_items
    return render(request, "admission.html", 
        {"page": "admission", "menu": menu_items})

def people(request):
    from academics.models import *
    global menu_items

    '''
    DEMO

    user = UserExtended(1)
    print user.type
    user.type = "student"
    print user.type
    user.save()

    #del user.age

    '''


    return render(request, "people.html", {"page": "people", "menu": menu_items})

def metakeys(request):
    fieldset = ['aaaaaaaa', 'bbbbbbbbb', 'cccccccccc']
    return render_to_response(
        "admin/academics/user/change_form.html", 
        RequestContext(request, {}))