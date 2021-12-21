from scene_management.scenes.announce import Announce

class Error(Announce):
    def __init__(self, master, body: str):
        super().__init__(master, "ERROR", body)
        self._title.config(fg="red")