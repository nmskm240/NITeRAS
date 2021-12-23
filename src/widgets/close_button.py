from widgets.image_button import ImageButton

class CloseButton(ImageButton):
    def __init__(self, master) -> None:
        super().__init__(master, "close")

    def _on_click(self) -> None:
        self.quit()