import tkinter as tk

from marshmallow.fields import Function
from scene_management.scene import Scene
from scene_management.scene_manager import SceneManager
from scene_management.scenes.result import Result

class Login(Scene): 
    do_login: Function(str)

    def __init__(self, master, do_login: Function(str) = None):
        super().__init__(master)
        self.do_login = do_login

    def on_load(self) -> None:
        sv = tk.StringVar()
        announce = tk.Label(self, text="学生証をかざしてください", font=("", 20))
        entry = tk.Entry(self, textvariable=sv)
        entry.focus_set()
        entry.bind("<Return>", func=lambda event: self.login_process(sv.get()))
        back = tk.Button(self, text="戻る", command=lambda: SceneManager.back())
        announce.pack()
        entry.pack()
        back.pack()

    def login_process(self, id: str) -> None:
        result = self.do_login(id)
        SceneManager.load(Result(self.master, result))
