from django.test import TestCase
from django.test.client import Client


class GeneralTest(TestCase):
    """ Test blog app """

    def setUp(self):
        self.client = Client()

    def _test_get(self, url, status_code, active_page=None, **kwargs):
        response = self.client.get(url, **kwargs)
        self.assertEqual(response.status_code, status_code)
        if active_page:
            self.assertEqual(response.context['activepage'], active_page)

    def test_index(self):
        self._test_get('/', 200, 'index')
        self._test_get('/index/', 200, 'index')

    def test_about(self):
        self._test_get('/about/', 200, 'About')

    def test_admission(self):
        self._test_get('/admission/', 200, 'Admission')

    def test_thankyou(self):
        self._test_get('/thankyou/', 200)
