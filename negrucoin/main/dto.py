from dataclasses import dataclass


@dataclass
class MoneyCountDto:
    money: int


@dataclass
class TopPlayerDto:
    avatar_url: str
    nickname: str
    coins: int


@dataclass
class TopPlayersDto:
    top_players: list[TopPlayerDto]
