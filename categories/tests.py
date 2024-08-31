from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Category
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class BaseCategoryTestCase(APITestCase):
    """
    Base class for category tests with common setup and utility methods.
    """

    def setUp(self):
        """
        Common setup for all category tests.
        """
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        # Obtain and set JWT token
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

        # Create a test category
        self.category = Category.objects.create(
            name='Test Category',
            description='A description for the test category'
        )
        self.valid_payload = {
            'name': 'New Category',
            'description': 'A description for the new category'
        }
        self.invalid_payload = {
            'name': '',
            'description': 'Invalid description'
        }
        self.list_url = reverse('category-list')
        self.detail_url = reverse('category-detail', args=[self.category.category_id])  # Use self.category.category_id

class CategoryTestCase(BaseCategoryTestCase):

    def test_create_category(self):
        """
        Given valid category data
        When creating a new category
        Then the category should be created
        And a 201 status code should be returned
        """
        response = self.client.post(self.list_url, self.valid_payload, format='json')
        print(response.data)  # Print response to debug
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)  # Ensure there are now two categories
        self.assertEqual(Category.objects.get(name='New Category').name, 'New Category')

    def test_create_category_with_invalid_data(self):
        """
        Given invalid category data
        When creating a new category
        Then the category should not be created
        And a 400 status code should be returned
        """
        response = self.client.post(self.list_url, self.invalid_payload, format='json')
        print(response.data)  # Print response to debug
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Category.objects.count(), 1)  # Ensure there is still only one category

    def test_read_category(self):
        """
        Given an existing category
        When retrieving the category
        Then the category details should be returned
        And a 200 status code should be returned
        """
        response = self.client.get(self.detail_url)
        print(response.data)  # Print response to debug
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Category')

    def test_update_category(self):
        """
        Given a category with existing data
        When updating the category with valid data
        Then the category should be updated
        And a 200 status code should be returned
        """
        update_payload = {
            'name': 'Updated Category',
            'description': 'A new description'
        }
        response = self.client.put(self.detail_url, update_payload, format='json')
        print(response.data)  # Print response to debug
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, 'Updated Category')

    def test_delete_category(self):
        """
        Given an existing category
        When deleting the category
        Then the category should be deleted
        And a 204 status code should be returned
        """
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)