from dataclasses import dataclass, field
from networks.dto_base import DTO

class MemberData(DTO):
    class DiscordData(DTO):
        id: str = ""
        nickname: str = ""
        tag: str = ""

    class Game(DTO):
        title: str = ""
        id: str = ""


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
        cls.DiscordData()
        cls.Game()
        #---------------
        return super().from_json(json)