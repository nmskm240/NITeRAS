from networks.access_point import AccessPoint
from networks.network import Network
from networks.requests.student_id import StudentID

class RoomAccessManager():
    @staticmethod
    def access(id: str):
        id = id.replace("A", "")
        if(id.isdigit()):
            dto = StudentID(int(id))
            member = Network.get(AccessPoint.NAME_LIST, dto)
