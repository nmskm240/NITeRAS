import os
from networks.access_point import AccessPoint
from networks.network import Network
from networks.requests.room_access_data import RoomAccessData, RoomAccessType
from networks.requests.student_id import StudentID

class RoomAccessManager():
    @staticmethod
    def access(id: str, access_type: RoomAccessType):
        id = id.replace("A", "")
        if(id.isdigit()):
            dto = StudentID(int(id))
            member = Network.get(AccessPoint.NAME_LIST, dto)
            access_data = RoomAccessData(member, os.environ["CAMPUS_NAME"], access_type)
            access_result = Network.post(AccessPoint.ROOM_ACCESS_LOG, access_data)
            print(access_result)