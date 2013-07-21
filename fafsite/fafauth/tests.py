from django.test import TestCase
from django.test.client import Client


class FafAuthTest(TestCase):
    def setUp(self):
        self.client = Client()
        # valid form fields
        self.name = 'foo'
        self.email = 'foo@example.org'
        self.message = 'lorem ipsum'

    def test_get_login_page(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)