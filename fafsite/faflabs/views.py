from django.shortcuts import render

def dashboard(request):
  return render(request, 'faflabs/dashboard.html', {})

def courses(request):
  return render(request, 'faflabs/dashboard.html', {})

def course(request, id):
  return render(request, 'faflabs/dashboard.html', {})

def lab(request, course_id, lab_number):
  return render(request, 'faflabs/dashboard.html', {})
