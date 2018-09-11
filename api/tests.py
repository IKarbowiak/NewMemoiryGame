from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class ViewTestCase(TestCase):
    """ Test suite for api views. """

    def setup(self):
        """ Define test client and other test variables. """
        self.client = APIClient()
        self.deck_data = {'name': 'deck_test'}
        self.response = self.client.post(
            reverse('create'),
            self.deck_data,
            format="json")

    def test_api_can_create_a_memocard(self):
        """" Test the api has memocard creation capability. """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)



