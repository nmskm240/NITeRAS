from networks.dto_base import DTO

class RoomAccessResult(DTO):
    state: str = ""
    message: str = ""

    @classmethod
    def from_json(cls, json) -> "RoomAccessResult":
        #事前に必要なインスタンスを作成しないとparseできなかったので記入
        #---------------
        RoomAccessResult()
        #---------------
        return super().from_json(json)