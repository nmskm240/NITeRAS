from dataclasses import dataclass
from enum import Enum
import os
from networks.responses.member_data import MemberData


@dataclass(frozen= True)
class AccessPointData():
    url: str
    get_res_type: type
    post_res_type: type

class AccessPoint(Enum):
    NAME_LIST = AccessPointData(os.environ["NAME_LIST_API_URL"], MemberData, None)
