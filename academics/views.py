from django.shortcuts import render, render_to_response
from django.template import RequestContext
from academics.models import *

menu_items = [
		('/about/', 'About'),
		('/admission/', 'Admission'),
		('/achievements/', 'Achievements'),
		('/activities/', 'Activities'),
		('/people/', 'People'),
		('/courses/', 'Courses'),
		('/contact-us/', 'Contact Us')
	]

def getCourses():
	semesters = ['I','II','III','IV','V','VI','VII']
	courses = []
	for sem in semesters:
		courses.append(Course.objects.filter(semester=sem))
	return courses


# Main page of courses blocks sorted by semesters
def courses(request):
	global menu_items
	courses = getCourses()
	return render(request, "courses.html", 
		{"activepage": "Courses", "menu": menu_items, "courses": courses})

# Page of a single course containing all the info about it
def about_course(request, course):
	global menu_items
	courses = getCourses()   
	try:
		course_info = Course.objects.get(title=course)
	except:
		raise Http404()
	return render(request, "about-course.html", 
			{"activepage": "Courses", "menu": menu_items, "courses": courses, "course":course_info})

# Main page of people
# Lists all the professors and their attributes
def professors(request):
	global menu_items
	academics = []
	professors = UserMeta.objects.filter(value='professor')
	for professor in professors:
		userID = professor.user_id
		# prof = User.objects.get(id=userID)
		prof = UserExtended(userID)
		courses = Course.objects.filter(professors=prof)
		academics.append([prof, courses])
	return render(request, "professors.html", 
		{"activepage": "People", "menu": menu_items, "academics": academics})

# Lists all the students filtered by the group with all their attributes
def students(request, group):
	global menu_items

	return render(request, "students.html", 
		{"activepage": "People", "menu": menu_items})

# Lists all the alumni filtered by the group with all their attributes
def alumni(request, group):
	global menu_items

	return render(request, "alumni.html", 
		{"activepage": "People", "menu": menu_items})