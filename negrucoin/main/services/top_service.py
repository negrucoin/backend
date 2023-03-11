import random

from main.dto import TopPlayersDto, TopPlayerDto


class TopService:
    @staticmethod
    def get_top_players(count: int = 10) -> TopPlayersDto:
        top_players = [
            TopPlayerDto(avatar_url='/media/logo.png',
                         nickname='Rally Og.',
                         coins=random.randint(15000, 20000)),
            TopPlayerDto(avatar_url='/media/logo2.png',
                         nickname='Hello',
                         coins=random.randint(10000, 15000)),
            TopPlayerDto(avatar_url='/media/logo3.png',
                         nickname='Джек Воробей',
                         coins=random.randint(5000, 10000)),
            TopPlayerDto(avatar_url='/media/logo4.png',
                         nickname='yay',
                         coins=random.randint(1000, 5000)),
        ]
        return TopPlayersDto(top_players=top_players[:count])
