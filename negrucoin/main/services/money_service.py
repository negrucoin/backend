from main.dto import MoneyCountDto
from main.models import Client


class MoneyService:
    @classmethod
    def get_client_money_count(cls, client: Client) -> MoneyCountDto:
        return MoneyCountDto(money=client.calculate_money())
