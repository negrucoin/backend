import pytest
from django.urls import reverse

from rest_framework.test import APIClient


@pytest.fixture()
def api_client():
    return APIClient()


def test_registration_request_is_success(api_client):
    response = api_client.post(
        reverse('sign-in'),
        {
            'nickname': 'Job',
            'password': 'myBESTpassword123',
            'confirm_password': 'myBESTpassword123',
        }
    )
    assert response.status_code == 200


def test_registration_request_small_password(api_client):
    response = api_client.post(
        reverse('sign-in'),
        {
            'nickname': 'fell_good',
            'password': 'sMa3lp',
            'confirm_password': 'sMa3lp',
        }
    )
    assert response.status_code == 401


def test_registration_request_without_nums(api_client):
    response = api_client.post(
        reverse('sign-in'),
        {
            'nickname': 'petri',
            'password': 'ONEtrueThink',
            'confirm_password': 'ONEtrueThink',
        }
    )
    assert response.status_code == 401


def test_registration_request_without_uppercase_letters(api_client):
    response = api_client.post(
        reverse('sign-in'),
        {
            'nickname': 'lolXD',
            'password': 'moo123its123cow',
            'confirm_password': 'moo123its123cow',
        }
    )
    assert response.status_code == 401
