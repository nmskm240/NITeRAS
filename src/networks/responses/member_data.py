from dataclasses import field
from networks.dto_base import DTO
from networks.responses.discord_data import DiscordData
from networks.responses.game import Game

class MemberData(DTO):
    id: int = -1
    name: str = ""
    role: str = ""
    discord: DiscordData = None
    games: list[Game] = None

    @classmethod
    def from_json(cls, json) -> "MemberData":
        #事前に必要なインスタンスを作成しないとparseできなかったので記入
        #---------------
        MemberData()
        DiscordData()
        Game()
        #---------------
        return super().from_json(json)