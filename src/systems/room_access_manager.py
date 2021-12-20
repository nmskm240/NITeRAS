import os
from networks.access_point import AccessPoint
from networks.network import Network
from networks.requests.room_access_data import RoomAccessData, RoomAccessType
from networks.requests.student_id import StudentID
from networks.responses.room_access_result import RoomAccessResult

class RoomAccessManager():
    @staticmethod
    def access(id: int, access_type: RoomAccessType) -> RoomAccessResult:
        dto = StudentID(id)
        member = Network.get(AccessPoint.NAME_LIST, dto)
        access_data = RoomAccessData(member, os.environ["CAMPUS_NAME"], access_type)
        access_result = Network.post(AccessPoint.ROOM_ACCESS_LOG, access_data)
        return access_result