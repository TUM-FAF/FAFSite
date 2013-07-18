from django.test import TestCase
from django.test.client import Client

from .models import Course, User
from .views import getCourses, get_groups


class AcademicsTest(TestCase):
    """ Test academics app """

    def setUp(self):
        self.client = Client()
        self.course_name = "course-name"
        self.sample_course = Course(title=self.course_name,
                                    subject_ro="Ro course name",
                                    subject_en="En course name",
                                    semester="I",
                                    language="EN",
                                    courseProject=False,
                                    labs=False)
        self.sample_course.save()

    def _test_get(self, url, status_code, active_page=None, **kwargs):
        response = self.client.get(url, **kwargs)
        self.assertEqual(response.status_code, status_code)
        if active_page:
            self.assertEqual(response.context['activepage'], active_page)

    def test_get_courses(self):
        courses = getCourses()
        self.assertIn(self.sample_course, courses[0])

    def test_get_groups(self):
        user = User(name="foo", surname="foofoo", email="foo@example.org",
                    group="FAF101")
        user.save()
        groups = get_groups()
        self.assertIn("FAF101", groups)

    def test_courses(self):
        self._test_get('/courses/', 200, 'Courses')

    def test_course(self):
        self._test_get('/courses/{0}/'.format(self.course_name), 200, 'Courses')

    def test_invalid_course(self):
        self._test_get('/courses/foo/', 404)

    def test_professors(self):
        self._test_get('/people/professors/', 200, 'People')

    def test_students(self):
        self._test_get('/people/students/faf101/', 200, 'People')

    def test_alumni(self):
        self._test_get('/people/alumni/faf061/', 200, 'People')
