from django.test import TestCase
from django.urls import reverse
from .models import Project

# Create your tests here.

class ProjectModelTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title='Proyecto de prueba',
            description='Descripción de prueba',
            git_hub='https://github.com/ejemplo',
            order=1
        )

    def test_project_str(self):
        self.assertEqual(str(self.project), 'Proyecto de prueba')

    def test_project_creation(self):
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(self.project.description, 'Descripción de prueba')

class PortfolioViewTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title='Proyecto de prueba',
            description='Descripción de prueba',
            git_hub='https://github.com/ejemplo',
            order=1
        )

    def test_portfolio_view_status_code(self):
        response = self.client.get(reverse('portfolio'))
        self.assertEqual(response.status_code, 200)

    def test_portfolio_view_uses_template(self):
        response = self.client.get(reverse('portfolio'))
        self.assertTemplateUsed(response, 'portfolio/portfolio.html')

    def test_projects_in_context(self):
        response = self.client.get(reverse('portfolio'))
        self.assertIn(self.project, response.context['projects'])
