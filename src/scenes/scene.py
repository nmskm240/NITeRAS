import tkinter as tk
from abc import ABCMeta, abstractmethod

class Scene(tk.Frame, metaclass=ABCMeta):
    def __init__(self, master= None):
        tk.Frame.__init__(self, master)
        self.on_load()

    @abstractmethod
    def on_load(self) -> None:
        pass