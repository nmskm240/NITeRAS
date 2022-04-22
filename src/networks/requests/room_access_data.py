from enum import Enum
from networks.dto_base import DTO
from networks.responses.member_data import MemberData

class Campus(str, Enum):
    OBASE = "小波瀬"
    KOKURA = "小倉"

class RoomAccessType(str, Enum):
    IN = "入室"
    OUT = "退室"

class RoomAccessData(DTO):
    class Member(DTO):
        class Discord(DTO):
            id: str = ""
            nickname: str = ""

        id: int = -1
        name: str = ""
        discord: Discord = None

    member: Member = None
    campus: Campus = Campus.OBASE
    type: RoomAccessType = RoomAccessType.IN

    def __init__(self, memberData: MemberData, campus: Campus, accessType: RoomAccessType):
        discord = self.Member.Discord(memberData.discord.id, memberData.discord.nickname)
        member = self.Member(memberData.id, memberData.name, discord)
        self.member = member
        self.campus = campus
        self.type = accessType