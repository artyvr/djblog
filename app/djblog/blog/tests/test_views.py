""" Test blog views """

from django.test import TestCase
from django.contrib.auth import get_user_model, authenticate
from blog.models import Post


class ViewsTestCase(TestCase):
    """ Views tests """

    def test_index_load(self):
        """The index (/blog/) page loads properly"""
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_tags_load(self):
        """The tags (/blog/tags/) page loads properly"""
        response = self.client.get('/blog/tags/')
        self.assertEqual(response.status_code, 200)

    def test_login_load(self):
        """ The login form (/accounts/login/) load """
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_admin_load(self):
        """The index (/admin/login/) page loads properly"""
        response = self.client.get('/admin/login/')
        self.assertEqual(response.status_code, 200)

    def test_create_tag_load(self):
        """ The create tag page load (/blog/tag/create/) (Permission Denied) """
        response = self.client.get('/blog/tag/create/')
        self.assertEqual(response.status_code, 403)

    def test_create_post_load(self):
        """ The create post page load (/blog/post/create/) (Permission Denied) """
        response = self.client.get('/blog/post/create/')
        self.assertEqual(response.status_code, 403)

    def test_post_detail_load(self):
        user = get_user_model().objects.create_user(
            username='test',
            password='23TestUser23',
            email='test@test.com')
        user.save()
        
        post = Post(title='Test post title',
                    body='Test post body',
                    user=user)
        post.save()

        post = Post.objects.get(title__iexact='Test post title')
        response = self.client.get(f'/blog/post/{post.slug}/')
        self.assertEqual(response.status_code, 200)
