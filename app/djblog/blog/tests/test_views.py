""" Test blog views """

from django.test import TestCase


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
