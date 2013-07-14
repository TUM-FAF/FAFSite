from django.test import TestCase
from django.test.client import Client


class BlogTest(TestCase):
    """ Test blog app """

    def setUp(self):
        self.client = Client()

    def _test_get(self, url, status_code, active_page=None, **kwargs):
        response = self.client.get(url, **kwargs)
        self.assertEqual(response.status_code, status_code)
        if active_page:
            self.assertEqual(response.context['activepage'], active_page)

    def test_achievements(self):
        self._test_get('/achievements/', 200, 'Achievements')

    def test_activities(self):
        self._test_get('/activities/', 200, 'Activities')
