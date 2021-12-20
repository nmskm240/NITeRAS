import tkinter as tk

from scene_management.scenes.announce import Announce

class Success(Announce):
    def __init__(self, master, body: str):
        super().__init__(master, "SUCCESS", body)
        self.title.config(fg="green")