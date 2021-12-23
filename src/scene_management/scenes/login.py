import tkinter as tk

from networks.requests.room_access_data import RoomAccessType
from scene_management.scene import Scene
from scene_management.scene_manager import SceneManager
from scene_management.scenes.complete import Complete
from scene_management.scenes.error import Error
from scene_management.scenes.loading import Loading
from systems.room_access_manager import RoomAccessManager
from widgets.back_button import BackButton

class Login(Scene): 
    def __init__(self, master, access_type: RoomAccessType):
        super().__init__(master)
        self.__access_type = access_type
        sv = tk.StringVar()
        entry = tk.Entry(self, textvariable=sv)
        entry.focus_set()
        entry.bind("<Return>", func=lambda event: SceneManager.load(
            Loading(self.master, lambda: self.__login_process(sv.get()))
        ))
        entry.place(x=0, y=0, height=1)
        back = BackButton(self)
        back.place(
            anchor=tk.SW, 
            x=0, 
            y=self.master.winfo_height()
        )

    def __login_process(self, id: str) -> None:
        id = id.replace("A", "")
        if(id.isdigit()):
            try:
                result = RoomAccessManager.access(int(id), self.__access_type)
                if(result.state == "SUCCESS"):
                    SceneManager.load(Complete(self.master, result.message))
                else:
                    SceneManager.load(Error(self.master, result.message))
            except Exception as e:
                SceneManager.load(Error(self.master, e))
        else:
            SceneManager.load(Error(self.master, "このバーコードは使用できません"))
