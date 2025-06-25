from django.test import TestCase
from django.urls import reverse
from .models import Pages

# Create your tests here.

class PagesModelTest(TestCase):
    def setUp(self):
        self.page = Pages.objects.create(
            title='Página de prueba',
            content='Contenido de prueba',
            order=1
        )

    def test_pages_str(self):
        self.assertEqual(str(self.page), 'Página de prueba')

    def test_pages_creation(self):
        self.assertEqual(Pages.objects.count(), 1)
        self.assertEqual(self.page.content, 'Contenido de prueba')

class PageDetailViewTest(TestCase):
    def setUp(self):
        self.page = Pages.objects.create(
            title='Página de prueba',
            content='Contenido de prueba',
            order=1
        )

    def test_page_detail_view_status_code(self):
        response = self.client.get(reverse('page', args=[self.page.id]))
        self.assertEqual(response.status_code, 200)

    def test_page_detail_view_uses_template(self):
        response = self.client.get(reverse('page', args=[self.page.id]))
        self.assertTemplateUsed(response, 'pages/pages.html')

    def test_page_in_context(self):
        response = self.client.get(reverse('page', args=[self.page.id]))
        self.assertEqual(response.context['page'], self.page)
