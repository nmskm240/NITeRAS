from networks.dto_base import DTO
from networks.responses.member_data import MemberData

class RoomAccessData(DTO):
    class Member(DTO):
        class Discord(DTO):
            id: str = ""

        id: int = -1
        name: str = ""
        discord: Discord = None

    member: Member = None
    campus: str = ""
    type: str = ""

    @classmethod
    def parse(cls, memberData: MemberData):
        discord = cls.Member.Discord(memberData.discord.id)
        member = cls.Member(memberData.id, memberData.name, discord)
        return RoomAccessData(member, "小波瀬", "入室")