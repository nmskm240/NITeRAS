import tkinter as tk

from networks.requests.room_access_data import RoomAccessType
from scene_management.scene import Scene
from scene_management.scene_manager import SceneManager
from scene_management.scenes.login import Login

class Home(Scene) :
    def __init__(self, master):
        super().__init__(master)
        buttons = tk.Label(self)
        room_in = tk.Button(
            buttons, 
            text="入室", 
            font=("", 80),
            fg="green",
            command= lambda: SceneManager.load(
                Login(self.master, RoomAccessType.IN)
            )
        )
        room_out = tk.Button(
            buttons, 
            text="退室",
            font=("", 80),
            fg="red",
            command= lambda: SceneManager.load(
                Login(self.master, RoomAccessType.OUT)
            )
        )
        room_in.pack(padx=20, side=tk.LEFT)
        room_out.pack(padx=20, side=tk.LEFT)
        buttons.place(x=0, y=0)