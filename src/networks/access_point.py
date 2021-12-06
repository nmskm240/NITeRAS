from dataclasses import dataclass
from enum import Enum
import os
from networks.responses.member_data import MemberData
from networks.responses.room_access_result import RoomAccessResult

@dataclass(frozen= True)
class AccessPointData():
    url: str
    get_res_type: type
    post_res_type: type

class AccessPoint(Enum):
    NAME_LIST = AccessPointData(os.environ["NAME_LIST_API_URL"], MemberData, None)
    ROOM_ACCESS_LOG = AccessPointData(os.environ["ROOM_ACCESS_API_URL"], None, RoomAccessResult)
