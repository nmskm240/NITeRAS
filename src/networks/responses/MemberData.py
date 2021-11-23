from dataclasses import field
from networks.dto_base import DTO
from networks.responses.DiscordData import DiscordData
from networks.responses.Game import Game

class MemberData(DTO):
    id: int = -1
    name: str = ""
    role: str = ""
    discord: DiscordData = None
    games: list[Game] = None

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        DiscordData.__new__(cls)
        Game.__new__(cls)
        return self

    @classmethod
    def from_json(cls, json) -> "MemberData":
        #事前に必要なインスタンスを作成しないとparseできなかったので記入
        #---------------
        MemberData()
        DiscordData()
        Game()
        #---------------
        return super().from_json(json)