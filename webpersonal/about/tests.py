from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import About

# Create your tests here.

class AboutModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.about = About.objects.create(
            title='Sobre mí',
            content='Contenido de prueba',
            author=self.user
        )

    def test_about_str(self):
        self.assertEqual(str(self.about), 'Sobre mí')

    def test_about_creation(self):
        self.assertEqual(About.objects.count(), 1)
        self.assertEqual(self.about.author.username, 'testuser')

class AboutViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.about = About.objects.create(
            title='Sobre mí',
            content='Contenido de prueba',
            author=self.user
        )

    def test_about_view_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_about_view_uses_template(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about/about.html')

    def test_about_in_context(self):
        response = self.client.get(reverse('about'))
        self.assertIn('about', response.context)
        self.assertEqual(response.context['about'], self.about)
