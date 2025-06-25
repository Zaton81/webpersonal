from django.test import TestCase
from django.urls import reverse
from .models import Books

# Create your tests here.

class BooksModelTest(TestCase):
    def setUp(self):
        self.book = Books.objects.create(
            title='Libro de prueba',
            sinopsis='Sinopsis de prueba',
            link_compra='https://ejemplo.com/compra',
        )

    def test_books_str(self):
        self.assertEqual(str(self.book), 'Libro de prueba')

    def test_books_creation(self):
        self.assertEqual(Books.objects.count(), 1)
        self.assertEqual(self.book.sinopsis, 'Sinopsis de prueba')

class LibrosViewTest(TestCase):
    def setUp(self):
        self.book = Books.objects.create(
            title='Libro de prueba',
            sinopsis='Sinopsis de prueba',
            link_compra='https://ejemplo.com/compra',
        )

    def test_libros_view_status_code(self):
        response = self.client.get(reverse('libros'))
        self.assertEqual(response.status_code, 200)

    def test_libros_view_uses_template(self):
        response = self.client.get(reverse('libros'))
        self.assertTemplateUsed(response, 'libros/libros.html')

    def test_libros_in_context(self):
        response = self.client.get(reverse('libros'))
        self.assertIn(self.book, response.context['books'])
