import tkinter as tk

from networks.requests.room_access_data import RoomAccessType
from scene_management.scene import Scene
from scene_management.scene_manager import SceneManager
from scene_management.scenes.error import Error
from scene_management.scenes.processing import Processing
from scene_management.scenes.success import Success
from systems.room_access_manager import RoomAccessManager

class Login(Scene): 
    def __init__(self, master, access_type: RoomAccessType):
        super().__init__(master)
        self.__access_type = access_type
        sv = tk.StringVar()
        announce = tk.Label(self, text="学生証をかざしてください", font=("", 20))
        entry = tk.Entry(self, textvariable=sv)
        entry.focus_set()
        entry.bind("<Return>", func=lambda event: SceneManager.load(
            Processing(self.master, lambda: self.__login_process(sv.get()))
        ))
        back = tk.Button(self, text="戻る", command=lambda: SceneManager.back())
        announce.pack()
        entry.pack()
        back.pack()

    def __login_process(self, id: str) -> None:
        id = id.replace("A", "")
        if(id.isdigit()):
            try:
                result = RoomAccessManager.access(int(id), self.__access_type)
                if(result.state == "SUCCESS"):
                    SceneManager.load(Success(self.master, result.message))
                else:
                    SceneManager.load(Error(self.master, result.message))
            except Exception as e:
                SceneManager.load(Error(self.master, e))
        else:
            SceneManager.load(Error(self.master, "このバーコードは使用できません"))
