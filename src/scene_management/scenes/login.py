import tkinter as tk

from marshmallow.fields import Function
from scene_management.scene import Scene
from scene_management.scene_manager import SceneManager
from systems.room_access_manager import RoomAccessManager

class Login(Scene): 
    do_login: Function(str)

    def __init__(self, master, do_login: Function(str) = None):
        super().__init__(master)
        self.do_login = do_login

    def on_load(self) -> None:
        self.sv = tk.StringVar()
        self.announce = tk.Label(self, text="学生証をかざしてください")
        self.entry = tk.Entry(self, textvariable=self.sv)
        self.entry.focus_set()
        self.entry.bind("<Return>", func=lambda event: self.do_login(self.sv.get()))
        self.back = tk.Button(self, text="戻る", command=lambda: SceneManager.back())
        self.announce.pack()
        self.entry.pack()
        self.back.pack()