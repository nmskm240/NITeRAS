import socket
import requests
from networks.access_point import AccessPoint
from networks.dto_base import DTO

class Network():
    @staticmethod
    def is_connection() -> bool:
        ip = socket.gethostbyname(socket.gethostname())
        return not ip == "127.0.0.1"

    @staticmethod
    def get(access_point: AccessPoint, req: DTO) -> DTO:
        if(not Network.is_connection()):
            raise Exception("Not connected to network")
        res = requests.get(access_point._value_.url, req.to_dict())
        if(res.status_code != 200 or res.text == "null" or access_point._value_.get_res_type is None):
            return None
        return access_point._value_.get_res_type.from_json(res.text)

    @staticmethod
    def post(access_point: AccessPoint, req: DTO) -> DTO:
        if(not Network.is_connection()):
            raise Exception("Not connected to network")
        res = requests.post(access_point._value_.url, json= req.to_dict())
        if(res.status_code != 200 or res.text == "null" or access_point._value_.post_res_type is None):
            return None
        return access_point._value_.post_res_type.from_json(res.text)