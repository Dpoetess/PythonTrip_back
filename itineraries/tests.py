from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from itineraries.models import Itinerary

class BaseTestCase(APITestCase):
    """
    Base class for tests with common setup and utility methods.
    """

    def setUp(self):
        """
        Common setup for all tests.
        """
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Define URL patterns
        self.itineraries_list_url = reverse('itineraries-list')
        self.itineraries_detail_url = 'itineraries-detail'
        self.itineraries_add_collaborator_url = 'itineraries-add-collaborator'
        self.itineraries_remove_collaborator_url = 'itineraries-remove-collaborator'

        # Create an example itinerary
        self.itinerary = Itinerary.objects.create(
            user=self.user,
            name="Test Itinerary",
            description="A test itinerary",
            is_collaborative=True
        )

class ItineraryTestCase(BaseTestCase):

    def test_create_itinerary(self):
        """
        Given valid itinerary data
        When creating a new itinerary
        Then the itinerary should be created
        And a 201 status code should be returned
        """
        data = {
            "name": "New Itinerary",
            "description": "Test itinerary creation",
            "is_collaborative": False
        }

        response = self.client.post(self.itineraries_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Itinerary.objects.count(), 2)  # Ensure that there are now two itineraries
        new_itinerary = Itinerary.objects.get(name="New Itinerary")
        self.assertEqual(new_itinerary.user, self.user)  # Ensure the user is associated with the new itinerary

    def test_update_itinerary(self):
        """
        Given valid update data
        When updating an existing itinerary
        Then the itinerary should be updated
        And a 200 status code should be returned
        """
        url = reverse(self.itineraries_detail_url, kwargs={'pk': self.itinerary.pk})

        data = {
            "name": "Updated Itinerary",
            "duration": "1 12:00:00",
            "description": "Updated description",
            "is_collaborative": True
        }

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_itinerary(self):
        """
        Given an existing itinerary
        When deleting the itinerary
        Then the itinerary should be deleted
        And a 204 status code should be returned
        """
        url = reverse(self.itineraries_detail_url, kwargs={'pk': self.itinerary.pk})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Itinerary.objects.count(), 0)  # Ensure that no itineraries are left

class CollaboratorTestCase(BaseTestCase):

    def test_add_collaborator(self):
        """
        Given a collaborator user
        When adding the collaborator to an itinerary
        Then the collaborator should be added
        And a 200 status code should be returned
        """
        collaborator = User.objects.create_user(username='collaborator', password='password123')
        data = {'email_or_username': collaborator.username}
        url = reverse(self.itineraries_add_collaborator_url, kwargs={'pk': self.itinerary.pk})

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.itinerary.collaborators.filter(id=collaborator.id).exists())

    def test_remove_collaborator(self):
        """
        Given a collaborator user added to an itinerary
        When removing the collaborator from the itinerary
        Then the collaborator should be removed
        And a 200 status code should be returned
        """
        collaborator = User.objects.create_user(username='collaborator', password='password123')
        self.itinerary.collaborators.add(collaborator)
        data = {'email_or_username': collaborator.username}
        url = reverse(self.itineraries_remove_collaborator_url, kwargs={'pk': self.itinerary.pk})

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(self.itinerary.collaborators.filter(id=collaborator.id).exists())