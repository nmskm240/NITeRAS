import tkinter as tk
from abc import ABCMeta, abstractmethod

class Scene(tk.Frame, metaclass=ABCMeta):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

    @abstractmethod
    def on_load(self) -> None:
        pass

    def on_show(self) -> None:
        pass

    def on_hide(self) -> None:
        pass

    def on_destroy(self) -> None:
        pass