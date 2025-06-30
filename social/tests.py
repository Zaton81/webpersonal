from django.test import TestCase, RequestFactory
from .models import Link
from .processors import ctx_dict

# Create your tests here.

class LinkModelTest(TestCase):
    def setUp(self):
        self.link = Link.objects.create(
            key='github',
            name='GitHub',
            url='https://github.com/usuario'
        )

    def test_link_str(self):
        self.assertEqual(str(self.link), 'GitHub')

    def test_link_creation(self):
        self.assertEqual(Link.objects.count(), 1)
        self.assertEqual(self.link.url, 'https://github.com/usuario')

class SocialContextProcessorTest(TestCase):
    def setUp(self):
        self.link = Link.objects.create(
            key='github',
            name='GitHub',
            url='https://github.com/usuario'
        )
        self.factory = RequestFactory()

    def test_ctx_dict_includes_links(self):
        request = self.factory.get('/')
        context = ctx_dict(request)
        self.assertIn('github', context)
        self.assertEqual(context['github'], 'https://github.com/usuario')
