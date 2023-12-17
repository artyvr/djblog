""" Test blog forms  """

from django.test import TestCase
from blog.forms import TagForm, PostForm
from blog.models import gen_slug

class FormsTestCase(TestCase):
    """ Forms tests """

    def test_tag_form(self):
        """ Test Tag form """
        form = TagForm(data={
            'title': 'Test',
            'slug': 'test'
        })
        self.assertTrue(form.is_valid())

    def test_post_form(self):
        """ Test Post form """
        form_title = 'Test post title'
        form = PostForm(data={
            'title': 'Test',
            'slug': gen_slug(form_title),
            'body': 'Test body text...'
        })
        self.assertTrue(form.is_valid())
