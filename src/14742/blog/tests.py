from django.test import TestCase
from .models import *


class AnimalTestCase(TestCase):

    def test_1_create_author(self):
        """Animals that can speak are correctly identified"""
        lion = Author.objects.create(name="lion")
        cat = Author.objects.create(name="cat")
        self.assertEqual(Author.objects.get(name='lion'), lion)
        self.assertEqual(Author.objects.get(name='cat'), cat)

    def test_2_create_blog_post(self):
        cat = Author.objects.create(name="cat")
        BlogPost.objects.create(title='sdfhdgh', body="fhsghsdgh", author=cat)
        post = BlogPost.objects.get(title='sdfhdgh')
        self.assertEqual(post.author, cat)

    def test_3_create_blog_post(self):
        cat = Author.objects.create(name='cat')
        post = BlogPost.objects.create(title='hello', body='my name is cat', author=cat)
        Comment.objects.create(text='sfgsgsgds', blog_post=post)
        Comment.objects.create(text='sfgsgs', blog_post=post)
        z = post.copy()
        self.assertNotEqual(z, post.id)
