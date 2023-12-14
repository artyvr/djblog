""" Test blog views """

from django.test import TestCase


class ViewsTestCase(TestCase):
    """ Views tests """
    def test_index_load(self):
        """The index page loads properly"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_tags_load(self):
        """The tags page loads properly"""
        response = self.client.get('/tags/')
        self.assertEqual(response.status_code, 200)
