import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient

User = get_user_model()


@pytest.fixture()
def user() -> User:
    return User.objects.get(pk=1)


@pytest.fixture()
def api_client(user):
    api_client = APIClient()
    api_client.force_authenticate(user=user)
    return api_client


@pytest.mark.django_db
def test_registration_request_is_success(api_client):
    response = api_client.post(
        reverse('sign-in'),
        {
            'username': 'Job',
            'password': 'myBESTpassword123',
            'confirm_password': 'myBESTpassword123',
        }
    )
    assert response.status_code == 302  # redirect to main page


@pytest.mark.django_db
def test_registration_request_small_password(api_client):
    response = api_client.post(
        reverse('sign-in'),
        {
            'username': 'fell_good',
            'password': 'sMa3lp',
            'confirm_password': 'sMa3lp',
        }
    )
    assert response.status_code == 401


@pytest.mark.django_db
def test_registration_request_without_nums(api_client):
    response = api_client.post(
        reverse('sign-in'),
        {
            'username': 'petri',
            'password': 'ONEtrueThink',
            'confirm_password': 'ONEtrueThink',
        }
    )
    assert response.status_code == 401


@pytest.mark.django_db
def test_registration_request_without_uppercase_letters(api_client):
    response = api_client.post(
        reverse('sign-in'),
        {
            'username': 'lolXD',
            'password': 'moo123its123cow',
            'confirm_password': 'moo123its123cow',
        }
    )
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_money_count(api_client, user):
    response = api_client.get(
        reverse('money-count')
    )
    assert response.status_code == 200
    assert isinstance(response.data, dict)
    assert 'money' in response.data


@pytest.mark.django_db
def test_get_money_count_with_unauthorized_user(api_client, user):
    api_client.logout()
    response = api_client.get(
        reverse('money-count')
    )
    assert response.status_code == 403
