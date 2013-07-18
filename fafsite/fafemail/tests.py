from django.test import TestCase
from django.test.client import Client
from django.forms import Form
from django.core import mail

from .models import Email


class FafemailTest(TestCase):
    """ Test fafemail app """

    def setUp(self):
        self.client = Client()
        # valid form fields
        self.name = 'foo'
        self.email = 'foo@example.org'
        self.message = 'lorem ipsum'

    def test_get_contact_page(self):
        response = self.client.get('/contact-us/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['activepage'], 'Contact Us')
        self.assertIsInstance(response.context['form'], Form)

    def test_contact_form_success(self):
        response = self.client.post('/contact-us/',
                                    {'name': self.name, 'email': self.email,
                                     'message': self.message})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/contact-us/thanks/')
        self.assertEqual(len(mail.outbox), 1)

        emails = Email.objects.all()
        email = Email.objects.get(email=self.email)
        self.assertEqual(len(emails), 1)
        self.assertIsNotNone(email)
        self.assertEqual(email.name, self.name)

    def test_contact_form_bot_failure(self):
        surname = 'bar'
        response = self.client.post('/contact-us/',
                                    {'name': self.name, 'surname': surname,
                                     'email': self.email,
                                     'message': self.message})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/contact-us/sorry/')
        self.assertEqual(len(mail.outbox), 0)

    def test_contact_form_empty(self):
        response = self.client.post('/contact-us/')
        error = "This field is required."
        self.assertFormError(response, 'form', 'email', error)
        self.assertFormError(response, 'form', 'message', error)

    def test_contact_form_invalid_email(self):
        response = self.client.post('/contact-us/',
                                    {'email': 'non_valid_email'})
        error = "Enter a valid email address."
        self.assertFormError(response, 'form', 'email', error)
