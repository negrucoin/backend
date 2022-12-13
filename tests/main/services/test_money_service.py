import pytest

from main.dto import MoneyCountDto
from main.services.money_service import MoneyService


@pytest.mark.django_db
def test_getting_client_money_count(client):
    result = MoneyService.get_client_money_count(client)
    assert isinstance(result, MoneyCountDto)
