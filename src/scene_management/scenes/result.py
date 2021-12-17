import tkinter as tk

from scene_management.scene import Scene
from networks.responses.room_access_result import RoomAccessResult
from scene_management.scene_manager import SceneManager

class Result(Scene) :
    def __init__(self, master, access_result: RoomAccessResult):
        super().__init__(master)
        self.access_result = access_result

    def on_load(self) -> None:
        result = tk.Label(self, text=self.access_result.state)
        message = tk.Label(self, text=self.access_result.message)
        result.pack()
        message.pack()
        self.after(200, func=lambda: [SceneManager.back(), SceneManager.back()])