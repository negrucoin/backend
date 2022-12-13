import datetime
from decimal import Decimal
from unittest import mock

import pytest
import pytz
from django.utils import timezone

from main.models import MoneySaleOffer
from settings import MONEY_PER_MINUTE, TIME_ZONE


@pytest.mark.django_db
@pytest.mark.parametrize('now_datetime,excepted_result',
                         [
                             ('2022-12-01 00:01', MONEY_PER_MINUTE),
                             ('2022-12-01 01:00', MONEY_PER_MINUTE * 60),
                             ('2022-12-02 00:00', MONEY_PER_MINUTE * 60 * 24),
                         ])
@mock.patch.object(timezone, 'now')
def test_client_calculate_money(mocked_now, now_datetime, excepted_result, client):
    mocked_now.return_value = datetime.datetime.strptime(now_datetime, '%Y-%m-%d %H:%M').replace(tzinfo=pytz.timezone(TIME_ZONE))
    client.user.date_joined = datetime.datetime(2022, 12, 1, tzinfo=pytz.timezone(TIME_ZONE))
    client.money_profit = 0
    assert client.calculate_money() == excepted_result


@pytest.mark.django_db
def test_client_calculate_money_but_client_travels_back_in_time(client):
    client.user.date_joined = datetime.datetime(3022, 1, 1, tzinfo=pytz.timezone(TIME_ZONE))

    with pytest.raises(AssertionError):
        client.calculate_money()


@pytest.mark.django_db
@pytest.mark.parametrize('pk,excepted_result',
                         [
                             (1, '0.001'),
                             (2, '0.4995'),
                             (3, '0.02'),
                         ])
def test_offer_one_coin_price(pk, excepted_result):
    offer = MoneySaleOffer.objects.get(pk=pk)
    assert offer.one_coin_price == Decimal(excepted_result)
