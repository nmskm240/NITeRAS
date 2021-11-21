import tkinter as tk
from abc import ABCMeta

class Scene(tk.Frame, metaclass=ABCMeta):
    def __init__(self, master= None):
        tk.Frame.__init__(self, master)
