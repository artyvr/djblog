""" Test models blog """

from django.test import TestCase
from django.contrib.auth import get_user_model, authenticate
from blog.models import Post, Tag


USER_NAME = 'test'
USER_PASSWORD = '23TestUser23'
USER_EMAIL = 'test@test.com'

class UserModelTestCase(TestCase):
    """ Users test """
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username=USER_NAME,
            password=USER_PASSWORD,
            email=USER_EMAIL)
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        """ Correct auth user """
        user = authenticate(username=USER_NAME, password=USER_PASSWORD)
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        """ Wrong username """
        user = authenticate(username='wrong', password=USER_PASSWORD)
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        """ Wrong user password """
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)


class PostModelTestCase(TestCase):
    """ Post tests """
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username=USER_NAME,
            password=USER_PASSWORD,
            email=USER_EMAIL)
        self.user.save()
        self.post = Post(title='Test post title',
                         body='Test post body',
                         user=self.user)
        self.post.save()

    def tearDown(self):
        self.post.delete()
        self.user.delete()

    def test_update_post(self):
        """ Update post test """
        self.post = Post.objects.get(title__iexact='Test post title')
        self.post.body = 'Update post text'
        self.post.save()



class TagModelTestCase(TestCase):
    """ Tag tests """

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username=USER_NAME,
            password=USER_PASSWORD,
            email=USER_EMAIL)
        self.user.save()
        self.tag = Tag(title='Tag',
                       slug='test-tag-2-slug',
                       user=self.user)
        self.tag.save()

    def tearDown(self):
        self.tag.delete()
        self.user.delete()

    def test_update_tag(self):
        """ Update tag test """
        self.tag = Tag.objects.get(title__iexact='Tag')
        self.tag.title = 'Tag 2'
        self.tag.save()
