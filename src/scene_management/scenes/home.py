import os
import tkinter as tk

from networks.requests.room_access_data import RoomAccessType
from scene_management.scene import Scene
from widgets.close_button import CloseButton
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
        close = CloseButton(buttons)
        login.grid(column=0, row=0, padx=50, pady=50)
        logout.grid(column=2, row=0, padx=50, pady=50)
        close.grid(column=0, row=1, padx=10, pady=10)
        buttons.place(x=0, y=0)