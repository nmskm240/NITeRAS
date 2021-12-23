from scene_management.scene_manager import SceneManager
from widgets.image_button import ImageButton

class BackButton(ImageButton):
    def __init__(self, master) -> None:
        super().__init__(master, "back")

    def _on_click(self) -> None:
        SceneManager.back()