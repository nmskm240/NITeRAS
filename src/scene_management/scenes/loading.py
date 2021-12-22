import tkinter as tk

from marshmallow.fields import Function
from tkinter import ttk
from threading import Thread
from scene_management.scene import Scene

class Loading(Scene):
    __task: Thread

    def __init__(self, master, task: Function):
        super().__init__(master)
        self.__task = Thread(target=task)
        process_label = tk.Label(self, text="処理中")
        progress_bar = ttk.Progressbar(self, mode="indeterminate")
        process_label.pack()
        progress_bar.pack()
        progress_bar.start(5)

    def on_load(self) -> None:
        self.__task.start()

    def on_destroy(self) -> None:
        self.__task.join()