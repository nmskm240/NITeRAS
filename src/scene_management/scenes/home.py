import tkinter as tk

from networks.requests.room_access_data import RoomAccessType
from scene_management.scene import Scene
from scene_management.scene_manager import SceneManager
from scene_management.scenes.login import Login
from systems.room_access_manager import RoomAccessManager

class Home(Scene) :
    def __init__(self, master):
        super().__init__(master)
        buttons = tk.Label(self)
        room_in = tk.Button(
            buttons, 
            text="入室", 
            font=("", 80),
            height=5,
            width=10,
            fg="green",
            command= lambda: SceneManager.load(
                Login(
                    self.master, 
                    do_login= lambda id: RoomAccessManager.access(id, RoomAccessType.IN)
                )
            )
        )
        room_out = tk.Button(
            buttons, 
            text="退室",
            font=("", 80),
            height=5,
            width=10,
            fg="red",
            command= lambda: SceneManager.load(
                Login(
                    self.master, 
                    do_login= lambda id: RoomAccessManager.access(id, RoomAccessType.OUT)
                )
            )
        )
        room_in.pack(padx=20, side=tk.LEFT)
        room_out.pack(padx=20, side=tk.LEFT)
        buttons.pack(pady=50, expand=True)