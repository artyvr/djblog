""" Test blog views """

from django.test import TestCase
from django.contrib.auth import get_user_model
from blog.models import Post, Tag

USER_NAME = 'test'
USER_PASSWORD = '23TestUser23'
USER_EMAIL = 'test@test.com'

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
        """ The post detail page load (GET /blog/post/<str:slug>/) """
        user = get_user_model().objects.create_user(
            username=USER_NAME,
            password=USER_PASSWORD,
            email=USER_EMAIL)
        user.save()
        post = Post(title='Test post title',
                    body='Test post body',
                    user=user)
        post.save()
        post = Post.objects.get(title__iexact='Test post title')
        response = self.client.get(f'/blog/post/{post.slug}/')
        self.assertEqual(response.status_code, 200)

    def test_post_update_load(self):
        """ The post update page load (GET /blog/post/<str:slug>/update/) """
        user = get_user_model().objects.create_user(
            username=USER_NAME,
            password=USER_PASSWORD,
            email=USER_EMAIL)
        user.save()
        post = Post(title='Test post title',
                    body='Test post body',
                    user=user)
        post.save()
        post = Post.objects.get(title__iexact='Test post title')
        self.client.login(username=USER_NAME, password=USER_PASSWORD)
        response = self.client.get(f'/blog/post/{post.slug}/update/')
        self.assertEqual(response.status_code, 200)

    def test_post_update(self):
        """ The post update submit (POST /blog/post/<str:slug>/update/) """
        user = get_user_model().objects.create_user(
            username=USER_NAME,
            password=USER_PASSWORD,
            email=USER_EMAIL)
        user.save()
        post = Post(title='Test post title',
                    body='Test post body',
                    user=user)
        post.save()
        post = Post.objects.get(title__iexact='Test post title')
        self.client.login(username=USER_NAME, password=USER_PASSWORD)
        response = self.client.post(f'/blog/post/{post.slug}/update/')
        self.assertEqual(response.status_code, 302)

    def test_post_delete_load(self):
        """ The post delete page load (GET /blog/post/<str:slug>/delete/) """
        user = get_user_model().objects.create_user(
            username=USER_NAME,
            password=USER_PASSWORD,
            email=USER_EMAIL)
        user.save()
        post = Post(title='Test post title',
                    body='Test post body',
                    user=user)
        post.save()
        post = Post.objects.get(title__iexact='Test post title')
        self.client.login(username=USER_NAME, password=USER_PASSWORD)
        response = self.client.get(f'/blog/post/{post.slug}/delete/')
        self.assertEqual(response.status_code, 200)

    def test_post_delete(self):
        """ The post delete submit (POST /blog/post/<str:slug>/delete/) """
        user = get_user_model().objects.create_user(
            username=USER_NAME,
            password=USER_PASSWORD,
            email=USER_EMAIL)
        user.save()
        post = Post(title='Test post title',
                    body='Test post body',
                    user=user)
        post.save()
        post = Post.objects.get(title__iexact='Test post title')
        self.client.login(username=USER_NAME, password=USER_PASSWORD)
        response = self.client.post(f'/blog/post/{post.slug}/delete/')
        self.assertEqual(response.status_code, 302)

    def test_tag_detail_load(self):
        """ The tag detail page load (GET /blog/tag/<str:slug>/) """
        user = get_user_model().objects.create_user(
            username=USER_NAME,
            password=USER_PASSWORD,
            email=USER_EMAIL)
        user.save()
        tag = Tag(title='Tag',
                  slug='test-tag-slug',
                  user=user)
        tag.save()
        tag = Tag.objects.get(title__iexact='Tag')
        response = self.client.get(f'/blog/tag/{tag.slug}/')
        self.assertEqual(response.status_code, 200)

    def test_tag_update_load(self):
        """ The tag update page load (GET /blog/tag/<str:slug>/update/) """
        user = get_user_model().objects.create_user(
            username=USER_NAME,
            password=USER_PASSWORD,
            email=USER_EMAIL)
        user.save()
        tag = Tag(title='Tag',
                  slug='test-tag-slug',
                  user=user)
        tag.save()
        tag = Tag.objects.get(title__iexact='Tag')
        self.client.login(username=USER_NAME, password=USER_PASSWORD)
        response = self.client.get(f'/blog/tag/{tag.slug}/update/')
        self.assertEqual(response.status_code, 200)

    def test_tag_delete_load(self):
        """ The tag delete page load (GET /blog/tag/<str:slug>/delete/) """
        user = get_user_model().objects.create_user(
            username=USER_NAME,
            password=USER_PASSWORD,
            email=USER_EMAIL)
        user.save()
        tag = Tag(title='Tag',
                  slug='test-tag-slug',
                  user=user)
        tag.save()
        tag = Tag.objects.get(title__iexact='Tag')
        self.client.login(username=USER_NAME, password=USER_PASSWORD)
        response = self.client.get(f'/blog/tag/{tag.slug}/delete/')
        self.assertEqual(response.status_code, 200)

    def test_tag_delete(self):
        """ The tag delete submit (POST /blog/tag/<str:slug>/delete/) """
        user = get_user_model().objects.create_user(
            username=USER_NAME,
            password=USER_PASSWORD,
            email=USER_EMAIL)
        user.save()
        tag = Tag(title='Tag',
                  slug='test-tag-slug',
                  user=user)
        tag.save()
        tag = Tag.objects.get(title__iexact='Tag')
        self.client.login(username=USER_NAME, password=USER_PASSWORD)
        response = self.client.post(f'/blog/tag/{tag.slug}/delete/')
        self.assertEqual(response.status_code, 302)
