from widgets.image_button import ImageButton

class SettingButton(ImageButton):
    def __init__(self, master) -> None:
        super().__init__(master, "setting")

    def _on_click(self) -> None:
        pass