from django.shortcuts import render
from django.http import HttpResponse



def index(request):
	item = [
		('/about/', '' ,'About'),
		('/admission/', '', 'Admission'),
		('#', '', 'Achievements'),
		('#', '', 'Activities'),
		('/people/', '', 'People'),
		('/courses/', '', 'Courses'),
		('#', '', 'Contact Us')]
	return render(request, "mainpage.html", {"list": item})

def about(request):
	item = [
		('/about/', 'active' ,'About'),
		('/admission/', '', 'Admission'),
		('#', '', 'Achievements'),
		('#', '', 'Activities'),
		('/people/', '', 'People'),
		('/courses/', '', 'Courses'),
		('#', '', 'Contact Us')]
	return render(request, "about.html", {"list": item})

def courses(request):
	item = [
		('/about/', '' ,'About'),
		('/admission/', '', 'Admission'),
		('#', '', 'Achievements'),
		('#', '', 'Activities'),
		('/people/', '', 'People'),
		('/courses/', 'active', 'Courses'),
		('#', '', 'Contact Us')]
	return render(request, "courses.html", {"list": item})

def about_course(request):
	item = [
		('/about/', '' ,'About'),
		('/admission/', '', 'Admission'),
		('#', '', 'Achievements'),
		('#', '', 'Activities'),
		('/people/', '', 'People'),
		('/courses/', 'active', 'Courses'),
		('#', '', 'Contact Us')]
	return render(request, "about-course.html", {"list": item})

def timeline(request):
	item = [
		('/about/', '' ,'About'),
		('/admission/', '', 'Admission'),
		('#', 'active', 'Achievements'),
		('#', '', 'Activities'),
		('/people/', '', 'People'),
		('/courses/', '', 'Courses'),
		('#', '', 'Contact Us')]
	return render(request, "timeline.html", {"list": item})

def admission(request):
	item = [
		('/about/', '' ,'About'),
		('/admission/', 'active', 'Admission'),
		('#', '', 'Achievements'),
		('#', '', 'Activities'),
		('/people/', '', 'People'),
		('/courses/', '', 'Courses'),
		('#', '', 'Contact Us')]
	return render(request, "admission.html", {"list": item})

def people(request):
	item = [
		('/about/', 'active' ,'About'),
		('/admission/', '', 'Admission'),
		('#', '', 'Achievements'),
		('#', '', 'Activities'),
		('/people/', 'active', 'People'),
		('/courses/', '', 'Courses'),
		('#', '', 'Contact Us')]
	return render(request, "people.html", {"list": item})