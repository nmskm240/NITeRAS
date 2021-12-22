import tkinter as tk
from abc import ABCMeta

class Scene(tk.Frame, metaclass=ABCMeta):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self._background = tk.PhotoImage(file=f"images\\backgrounds\\{self.__class__.__name__.lower()}.png")
        photo_label = tk.Label(self, image=self._background)
        photo_label.pack()

    def on_load(self) -> None:
        pass

    def on_show(self) -> None:
        pass

    def on_hide(self) -> None:
        pass

    def on_destroy(self) -> None:
        pass