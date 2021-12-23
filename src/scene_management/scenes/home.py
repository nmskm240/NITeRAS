import os
import tkinter as tk

from networks.requests.room_access_data import RoomAccessType
from scene_management.scene import Scene
from widgets.room_access_button import RoomAccessButton

class Home(Scene) :
    def __init__(self, master):
        super().__init__(master)
        buttons = tk.Label(self)
        login = RoomAccessButton(
            buttons,
            RoomAccessType.IN
        )
        logout = RoomAccessButton(
            buttons, 
            RoomAccessType.OUT
        )
        login.pack(padx=20, side=tk.LEFT)
        logout.pack(padx=20, side=tk.LEFT)
        buttons.place(x=0, y=0)