from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Posts, Category
from datetime import datetime

# Create your tests here.

class BlogModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.category = Category.objects.create(name='Django')
        self.post = Posts.objects.create(
            title='Primer post',
            content='Contenido de prueba',
            author=self.user,
            published=datetime.now()
        )
        self.post.categories.add(self.category)

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Django')

    def test_post_str(self):
        self.assertEqual(str(self.post), 'Primer post')

    def test_post_category_relation(self):
        self.assertIn(self.category, self.post.categories.all())

class BlogViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.category = Category.objects.create(name='Django')
        self.post = Posts.objects.create(
            title='Primer post',
            content='Contenido de prueba',
            author=self.user,
            published=datetime.now()
        )
        self.post.categories.add(self.category)

    def test_blog_list_view(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/posts_list.html')
        self.assertIn(self.post, response.context['posts_list'])

    def test_post_detail_view(self):
        response = self.client.get(reverse('post', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post.html')
        self.assertEqual(response.context['post'], self.post)

    def test_category_view(self):
        response = self.client.get(reverse('category', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/category.html')
        self.assertIn(self.post, response.context['posts'])
