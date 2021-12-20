from playsound import playsound
from scene_management.scenes.announce import Announce

class Error(Announce):
    def __init__(self, master, body: str):
        super().__init__(master, "ERROR", body)
        self.title.config(fg="red")

    def on_load(self) -> None:
        playsound("sounds\error.mp3")
        return super().on_load()
