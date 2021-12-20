import tkinter as tk
from abc import ABCMeta

from scene_management.scene import Scene
from scene_management.scene_manager import SceneManager

class Announce(Scene, metaclass=ABCMeta):
    def __init__(self, master, title: str, body: str):
        super().__init__(master)
        self.title = tk.Label(self, text=title, font=("", 20))
        self.body = tk.Label(self, text=body)
        self.title.pack()
        self.body.pack()

    def on_load(self) -> None:
        self.after(1000, func=lambda: SceneManager.back_root())