from django.shortcuts import render
from django.http import Http404
from academics.models import *
from shared import get_menu_items
import operator

menu_items = get_menu_items()


def getCourses():
    semesters = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
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
            {"activepage": "Courses", "menu": menu_items, "courses": courses, "Course": course_info})


# Main page of people
# Ge a list of all distinct groups
def get_groups():
    group_dict = User.objects.values('group').distinct()
    groups = []
    for group in group_dict:
        if group['group'] != '' and group['group'] not in groups:
            groups.append(group['group'])
    groups = sorted(groups, reverse=True)
    return groups


# Lists all the professors and their attributes
def professors(request):
    global menu_items
    academics = []
    professors = UserMeta.objects.filter(value='professor')
    for professor in professors:
        userID = professor.user_id
        prof = UserExtended(userID)
        courses = Course.objects.filter(professors=prof)
        academics.append([prof, courses])
    groups = get_groups()
    student_groups = groups[:4]
    alumni_groups = groups[4:]
    return render(request, "professors.html",
        {"activepage": "People", "menu": menu_items, "academics": academics,
        'student_groups': student_groups, 'alumni_groups': alumni_groups})


# Lists all the students filtered by the group with all their attributes
def students(request, group):
    global menu_items
    students = []
    student_metas = UserMeta.objects.filter(value='student')
    for student in student_metas:
        userID = student.user_id
        st = UserExtended(userID)
        if st.group == group:
            students.append(st)

    students.sort(key=operator.attrgetter('surname'))

    groups = get_groups()
    student_groups = groups[:4]
    alumni_groups = groups[4:]
    return render(request, "students.html",
        {"activepage": "People", "menu": menu_items, "students": students, "this_group": group,
        'student_groups': student_groups, 'alumni_groups': alumni_groups})


# Lists all the alumni filtered by the group with all their attributes
def alumni(request, group):
    global menu_items
    alumni = []
    alumni_metas = UserMeta.objects.filter(value='alumni')
    for alumnae in alumni_metas:
        userID = alumnae.user_id
        al = UserExtended(userID)
        if al.group == group:
            alumni.append(al)

    alumni.sort(key=operator.attrgetter('surname'))

    groups = get_groups()
    student_groups = groups[:4]
    alumni_groups = groups[4:]
    return render(request, "alumni.html",
        {"activepage": "People", "menu": menu_items, "alumni": alumni, "this_group": group,
        'student_groups': student_groups, 'alumni_groups': alumni_groups})
