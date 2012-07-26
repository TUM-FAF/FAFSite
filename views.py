from django.shortcuts import render
from django.http import HttpResponse



def index(request):
	return render(request, "mainpage.html")

def about(request):
	return render(request, "about.html")

def courses(request):
	return render(request, "courses.html")

def about_course(request):
	return render(request, "about-course.html")