import datetime
from enum import Enum
from networks.dto_base import DTO

class RoomState(str, Enum):
    IN = "入室",
    OUT = "退室"

class LogData(DTO):
    id: int
    name: str
    state: RoomState
