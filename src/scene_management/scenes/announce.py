import tkinter as tk
from abc import ABCMeta

from scene_management.scene import Scene
from scene_management.scene_manager import SceneManager

class Announce(Scene, metaclass=ABCMeta):
    def __init__(self, master, message: str):
        super().__init__(master)
        self._message = message

    def on_load(self) -> None:
        self.after(2500, func=lambda: SceneManager.back_root())