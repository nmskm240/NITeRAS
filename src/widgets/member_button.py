from widgets.image_button import ImageButton

class MemberButton(ImageButton):
    def __init__(self, master) -> None:
        super().__init__(master, "member")

    def _on_click(self) -> None:
        pass