from django.test import TestCase
from .models import *


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='Tary', password='1234rrrr')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()


class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Tary')
        self.post = Post.objects.create(id=1, title='test post', image='', description='awesome',
                                        developer=self.user, url='')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        

    def test_get_posts(self):
        self.post.save()
        posts = Post.all_posts()
        

    def test_search_post(self):
        self.post.save()
        post = Post.search_project('test')

    def test_delete_post(self):
        self.post.delete_post()
        post = Post.search_project('test')


class RatingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Tary')
        self.post = Post.objects.create(id=1, title='test post', image='', description='awesome',
                                        developer=self.user, url='')
        self.rating = Rating.objects.create(id=1, design=10, usability=10, content=10, user=self.user, post=self.post)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Rating.objects.all()
