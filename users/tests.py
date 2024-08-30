from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

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
        self.client.force_authenticate(user=self.user)  # Authenticate by default

        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user_detail_url = reverse('user_detail')

        # Valid and invalid data for login
        self.valid_login_data = {
            'username': 'testuser',
            'password': 'password123'
        }
        self.invalid_login_data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }

        # Data for user registration
        self.registration_data = {
            'first_name': 'New',
            'last_name': 'User',
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123'
        }

        self.invalid_registration_data = {
            'first_name': '',
            'last_name': '',
            'username': 'newuser',
            'email': 'invalid-email',
            'password': 'short'
        }

    def authenticate_user(self):
        """
        Authenticate the test client with the created user.
        """
        self.client.force_authenticate(user=self.user)

class UserRegistrationTestCase(BaseTestCase):

    def test_register_user(self):
        """
        Given valid user data
        When registering a new user
        Then the user should be created
        And a 201 status code should be returned
        """
        response = self.client.post(self.register_url, self.registration_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)  # Ensure there are now two users
        self.assertEqual(User.objects.get(username='newuser').username, 'newuser')

    def test_register_user_with_invalid_data(self):
        """
        Given invalid user data
        When registering a new user
        Then the user should not be created
        And a 400 status code should be returned
        """
        response = self.client.post(self.register_url, self.invalid_registration_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)  # Ensure the count remains the same

class UserAuthTestCase(BaseTestCase):

    def test_login_user(self):
        """
        Given valid login credentials
        When logging in
        Then a token should be returned
        And a 200 status code should be returned
        """
        response = self.client.post(self.login_url, self.valid_login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_login_user_with_invalid_credentials(self):
        """
        Given invalid login credentials
        When logging in
        Then a token should not be returned
        And a 401 status code should be returned
        """
        response = self.client.post(self.login_url, self.invalid_login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class UserDetailTestCase(BaseTestCase):

    def test_get_user_details(self):
        """
        Given an authenticated user
        When requesting user details
        Then the user details should be returned
        And a 200 status code should be returned
        """
        response = self.client.get(self.user_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')

    def test_get_user_details_without_authentication(self):
        """
        Given no authentication
        When requesting user details
        Then a 403 status code should be returned
        """
        self.client.force_authenticate(user=None)  # De-authenticate
        response = self.client.get(self.user_detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)