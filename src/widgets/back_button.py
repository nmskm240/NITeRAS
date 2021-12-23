import os
import tkinter as tk
from scene_management.scene_manager import SceneManager
from widgets.image_button import ImageButton

class BackButton(ImageButton):
    def __init__(self, master) -> None:
        image_path = "resources\\images\\widgets\\back.png"
        image = tk.PhotoImage(file=os.path.abspath(image_path))
        super().__init__(master, image)

    def _on_click(self) -> None:
        SceneManager.back()