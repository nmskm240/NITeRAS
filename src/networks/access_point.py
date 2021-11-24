from dataclasses import dataclass
from enum import Enum
from networks.responses.member_data import MemberData


@dataclass(frozen= True)
class AccessPointData():
    env: str
    get_res_type: type
    post_res_type: type

class AccessPoint(Enum):
    NAME_LIST = AccessPointData("NAME_LIST_API_URL", MemberData, None)
    ROOM_ACCESS_LOG = AccessPointData("ROOM_ACESSS_LOG_API_URL", None, None)
