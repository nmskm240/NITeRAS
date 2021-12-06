from networks.access_point import AccessPoint
from networks.network import Network
from networks.requests.room_access_data import Campus, RoomAccessData, RoomAccessType
from networks.requests.student_id import StudentID

class RoomAccessManager():
    @staticmethod
    def access(id: str):
        id = id.replace("A", "")
        if(id.isdigit()):
            dto = StudentID(int(id))
            member = Network.get(AccessPoint.NAME_LIST, dto)
            access_data = RoomAccessData(member, Campus.OBASE, RoomAccessType.OUT)
            access_result = Network.post(AccessPoint.ROOM_ACCESS_LOG, access_data)
            print(access_result)