import tkinter as tk
from scene_management.scene import Scene
from scene_management.scene_manager import SceneManager
from systems.room_access_manager import RoomAccessManager

class Login(Scene): 
    def on_load(self) -> None:
        self.sv = tk.StringVar();
        self.announce = tk.Label(self, text="学生証をかざしてください")
        self.entry = tk.Entry(self, textvariable=self.sv)
        self.entry.focus_set()
        self.entry.bind("<Return>", func=lambda event: RoomAccessManager.access(self.sv.get()))
        self.back = tk.Button(self, text="戻る", command=lambda: SceneManager.back())
        self.announce.pack()
        self.entry.pack()
        self.back.pack()