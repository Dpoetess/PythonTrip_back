"""import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from itineraries.models import Itinerary
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='password123')

@pytest.fixture
def create_itinerary(user):
    return Itinerary.objects.create(
        user=user,
        name="Test Itinerary",
        duration="2 00:00:00",
        description="A test itinerary",
        is_collaborative=True
    )

@pytest.mark.django_db
def test_create_itinerary(api_client, user):
    token = Token.objects.create(user=user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    url = reverse('itineraries-list')

    data = {
        "name": "New Itinerary",
        "duration": "1 00:00:00",
        "description": "Test itinerary creation",
        "is_collaborative": False
    }

    response = api_client.post(url, data, format='json')
    print(response.data)  # Imprime el contenido del error para depuración
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_update_itinerary(api_client, user, create_itinerary):
    token = Token.objects.create(user=user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    url = reverse('itineraries-detail', kwargs={'pk': create_itinerary.itin_id})

    data = {
        "name": "Updated Itinerary",
        "duration": "1 12:00:00",  # Asegúrate de que este formato es correcto
        "description": "Updated description",
        "is_collaborative": True
    }

    response = api_client.put(url, data, format='json')
    print(response.data)  # Imprime el contenido del error para depuración
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_delete_itinerary(api_client, user, create_itinerary):
    token = Token.objects.create(user=user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    url = reverse('itineraries-detail', kwargs={'pk': create_itinerary.itin_id})

    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Itinerary.objects.count() == 0

@pytest.mark.django_db
def test_add_collaborator(api_client, user, create_itinerary):
    collaborator = User.objects.create_user(username='collaborator', password='password123')
    token = Token.objects.create(user=user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    url = reverse('itineraries-add-collaborator', kwargs={'pk': create_itinerary.itin_id})

    data = {'email_or_username': collaborator.username}
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert create_itinerary.collaborators.filter(id=collaborator.id).exists()

@pytest.mark.django_db
def test_remove_collaborator(api_client, user, create_itinerary):
    collaborator = User.objects.create_user(username='collaborator', password='password123')
    create_itinerary.collaborators.add(collaborator)
    token = Token.objects.create(user=user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    url = reverse('itineraries-remove-collaborator', kwargs={'pk': create_itinerary.itin_id})

    data = {'email_or_username': collaborator.username}
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert not create_itinerary.collaborators.filter(id=collaborator.id).exists()"""