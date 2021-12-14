import tkinter as tk
from networks.requests.room_access_data import RoomAccessType
from scene_management.scene import Scene
from scene_management.scene_manager import SceneManager
from scene_management.scenes.login import Login
from systems.room_access_manager import RoomAccessManager

class Home(Scene) :
    def on_load(self) -> None:
        self.room_in = tk.Button(
            self, 
            text="入室", 
            command= lambda: SceneManager.load(
                Login(
                    self.master, 
                    do_login= lambda id: RoomAccessManager.access(id, RoomAccessType.IN)
                )
            )
        )
        self.room_out = tk.Button(
            self, 
            text="退室",
            command= lambda: SceneManager.load(
                Login(
                    self.master, 
                    do_login= lambda id: RoomAccessManager.access(id, RoomAccessType.OUT)
                )
            )
        )
        self.room_in.pack()
        self.room_out.pack()