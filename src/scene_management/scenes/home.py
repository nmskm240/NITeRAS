import tkinter as tk
from scene_management.scene import Scene
from scene_management.scene_manager import SceneManager
from scene_management.scenes.login import Login

class Home(Scene) :
    def on_load(self) -> None:
        self.room_in = tk.Button(self, text="入室", command= lambda: SceneManager.load(Login(self.master)))
        self.room_out = tk.Button(self, text="退室")
        self.room_in.pack()
        self.room_out.pack()