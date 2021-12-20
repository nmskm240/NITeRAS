from playsound import playsound
from scene_management.scenes.announce import Announce

class Success(Announce):
    def __init__(self, master, body: str):
        super().__init__(master, "SUCCESS", body)
        self.title.config(fg="green")

    def on_load(self) -> None:
        playsound("sounds/success.mp3")
        return super().on_load()