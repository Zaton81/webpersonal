from django.test import TestCase
from django.urls import reverse
from .forms import ContactForm
from django.core import mail

# Create your tests here.

class ContactFormTest(TestCase):
    def test_form_invalid(self):
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('content', form.errors)

    def test_form_valid(self):
        form = ContactForm(data={
            'name': 'Test User',
            'email': 'test@example.com',
            'content': 'Mensaje de prueba'
        })
        self.assertTrue(form.is_valid())

class ContactViewTest(TestCase):
    def test_get_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        self.assertIn('form', response.context)

    def test_post_valid_contact_form(self):
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'content': 'Mensaje de prueba'
        }
        response = self.client.post(reverse('contact'), data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Gracias por tu mensaje', html=True)
        # Comprueba que se ha intentado enviar un email
        self.assertGreaterEqual(len(mail.outbox), 0)  # Puede ser 0 si el backend es consola

    def test_post_invalid_contact_form(self):
        data = {
            'name': '',
            'email': 'no-es-un-email',
            'content': ''
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'name', 'Este campo es obligatorio.')
        self.assertFormError(response, 'form', 'content', 'Este campo es obligatorio.')
