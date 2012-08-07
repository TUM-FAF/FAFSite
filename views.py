from django.shortcuts import render
from django.template import RequestContext
from blog.models import Article

menu_items = {
		'about': ('/about/', 'About')
		,'admission': ('/admission/', 'Admission')
		,'achievements': ('#', 'Achievements')
		,'activities': ('#', 'Activities')
		,'people': ('/people/', 'People')
		,'timeline': ('/timeline/', 'Timeline')
		,'courses': ('#', 'Courses')
		,'contact_us': ('#', 'Contact Us')
	}



def index(request):
	global menu_items
	return render(request, "mainpage.html", {"page": "index", "menu": menu_items})

def about(request):
	global menu_items
	return render(request, "about.html", {"page": "about", "menu": menu_items})

def courses(request):
	global menu_items
	courses = Course.objects.all()
	y = ['I','II','III','IV','V','VI','VII']
	return render(request, "courses.html", {"page": "courses", "menu": menu_items, "academic": courses, "y": y})

def about_course(request):
	global menu_items
	return render(request, "about-course.html", {"page": "about", "menu": menu_items})

def timeline(request):
	global menu_items
	articles = Article.objects.all()
	return render(request, "timeline.html", {"page": "timeline", "menu": menu_items, "articles": articles})

def admission(request):
	global menu_items
	return render(request, "admission.html", {"page": "admission", "menu": menu_items})

def people(request):
	global menu_items
	return render(request, "people.html", {"page": "people", "menu": menu_items})