import operator

from django.shortcuts import render
from django.http import Http404

from .models import Course, User, UserMeta, UserExtended


def getCourses():
    semesters = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    courses = []
    for sem in semesters:
        courses.append(Course.objects.filter(semester=sem))
    return courses


# Main page of courses blocks sorted by semesters
def courses(request):
    courses = getCourses()
    return render(request, "courses.html",
                  {"activepage": "Courses", "courses": courses})


# Page of a single course containing all the info about it
def about_course(request, course):
    courses = getCourses()
    try:
        course_info = Course.objects.get(title=course)
    except:
        raise Http404()
    return render(request, "about-course.html",
                  {"activepage": "Courses", "courses": courses, "Course": course_info})


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
    academics = []
    professors = UserMeta.objects.filter(value='professor')
    for professor in professors:
        userID = professor.user_id
        prof = UserExtended(userID).getAttributesAndValues()
        prof['courses'] = Course.objects.filter(professors=UserExtended(userID))
        academics.append(prof)

    groups = get_groups()
    student_groups = groups[:4]
    alumni_groups = groups[4:]
    return render(request, "people-list.html",
                  {"activepage": "People",
                   "container_title": "Professors",
                   "people": academics,
                   'student_groups': student_groups,
                   'alumni_groups': alumni_groups})


# Lists all the students filtered by the group with all their attributes
def students(request, group):
    students = []
    # TODO retrieve students by group
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
    return render(request, "people-list.html",
                  {"activepage": "People",
                   "container_title": "Students",
                   "people": students, "this_group": group,
                   'student_groups': student_groups,
                   'alumni_groups': alumni_groups})


# Lists all the alumni filtered by the group with all their attributes
def alumni(request, group):
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
    return render(request, "people-list.html",
                  {"activepage": "People",
                   "container_title": "Alumni",
                   "people": alumni, "this_group": group,
                   'student_groups': student_groups,
                   'alumni_groups': alumni_groups})
