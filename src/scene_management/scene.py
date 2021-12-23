import tkinter as tk
from abc import ABCMeta

from utils.misc_helper import MiscHelper

class Scene(tk.Frame, metaclass=ABCMeta):
    def __init__(self, master):
        master = MiscHelper.get_root(master)
        tk.Frame.__init__(self, master)
        image_path = f"./resources/images/backgrounds/{self.__class__.__name__.lower()}.png"
        self.__background = tk.PhotoImage(file=image_path)
        photo_label = tk.Label(self, image=self.__background)
        photo_label.pack()

    def on_load(self) -> None:
        pass

    def on_show(self) -> None:
        pass

    def on_hide(self) -> None:
        pass

    def on_destroy(self) -> None:
        pass