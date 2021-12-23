import os
import tkinter as tk

from scene_management.scene_manager import SceneManager
from scene_management.scenes.login import Login
from widgets.image_button import ImageButton
from networks.requests.room_access_data import RoomAccessType

class RoomAccessButton(ImageButton):
    def __init__(self, master, access_type: RoomAccessType) -> None:
        image_name = "login" if access_type == RoomAccessType.IN else "logout"
        image_path = f"resources\\images\\widgets\\{image_name}.png"
        image = tk.PhotoImage(file=os.path.abspath(image_path))
        super().__init__(master, image)
        self.__access_type = access_type

    def _on_click(self) -> None:
        SceneManager.load(Login(self.root(), self.__access_type))