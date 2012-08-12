from django.shortcuts import render, render_to_response
from django.template import RequestContext
from blog.models import Article
from django.core.mail import send_mail
from django.http import HttpResponseForbidden
# from django.views.decorators.csrf import csrf_exempt

menu_items = [
        ('/about/', 'About'),
        ('/admission/', 'Admission'),
        ('/achievements/', 'Achievements'),
        ('/activities/', 'Activities'),
        ('/people/', 'People'),
        ('#', 'Courses'),
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

def courses(request):
    global menu_items
    courses = Course.objects.all()
    y = ['I','II','III','IV','V','VI','VII']
    return render(request, "courses.html", 
        {"activepage": "Courses", "menu": menu_items, "academic": courses, "y": y})

def about_course(request):
    global menu_items
    return render(request, "about-course.html", 
        {"activepage": "About", "menu": menu_items})

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

def admission(request):
    global menu_items
    return render(request, "admission.html", 
        {"activepage": "Admission", "menu": menu_items})

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


    return render(request, "people.html", 
        {"activepage": "People", "menu": menu_items})
# TODO check the validity of the email address

def contact_us(request):
    global menu_items
    return render(request, "contact-us.html", 
        {"activepage": "Contact Us", "menu": menu_items})


# @csrf_exempt
def submit(request):
    response = ''
    # if 'name' in request.POST:
    #     result = "Your name is %s" % request.POST['name']
    if not request.POST:
        return HttpResponseForbidden()

    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    if email and message:
        message = '\n\nFROM: ' + email + '\n\nName: ' + name + '\n\nMessage: ' + message
        try:
            send_mail('[FAF]Contact us', message, email, ['ana.balica@gmail.com'], fail_silently=False)
            response = '<span>*</span> Thank you. We will consider your message as soon as possible and contact you.'
        except:
            return HttpResponse('Invalid header found.')
        """
        from startapp.models import Mail
        p = Mail(from_email = from_email , subject = subject, message = message)
        p.save()
        """
    else:
        if not email:
            pass
    return render(request, "contact-us.html", {"activepage": "Contact Us", "menu": menu_items, "response": response})