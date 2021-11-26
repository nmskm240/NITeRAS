import tkinter as tk
from networks.access_point import AccessPoint
from networks.network import Network
from networks.requests.log_data import LogData, RoomState
from networks.requests.student_id import StudentID
from scene_management.scene import Scene
from scene_management.scene_manager import SceneManager

class Login(Scene): 
    def enrollment_check(self) -> None:
        dto = StudentID(int(self.entry.get()))
        member = Network.get(AccessPoint.NAME_LIST, dto)
        Network.post(AccessPoint.ROOM_ACCESS_LOG, LogData(member.id, member.name, RoomState.IN))

    def on_load(self) -> None:
        self.entry = tk.Entry(self)
        self.result = tk.Label(self)
        self.submit = tk.Button(self, text="送信", command=lambda: self.enrollment_check())
        self.back = tk.Button(self, text="戻る", command=lambda: SceneManager.back())
        self.result.pack()
        self.entry.pack()
        self.submit.pack()
        self.back.pack()