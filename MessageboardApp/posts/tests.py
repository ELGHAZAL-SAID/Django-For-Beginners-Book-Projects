from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just a test')
    
    def test_text_content(self):
        Post.objects.create(text= 'just a test')


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is another test')
    
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
    
    def test_view_users_correct_temp(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'htmlPages/home.html')