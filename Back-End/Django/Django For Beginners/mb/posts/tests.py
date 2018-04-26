from django.test import TestCase

# Create your tests here.
# posts/tests.py
from django.test import TestCase
from .models import Post
from django.test import TestCase
from django.urls import reverse
from .models import Post



class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up data for our Test Case
        Post.objects.create(text='just a test')

    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEquals(expected_object_name, 'just a test')



class HomePageViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Post.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEquals(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEquals(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')