import tkinter as tk

from marshmallow.fields import Function
from scene_management.scene import Scene
from scene_management.scene_manager import SceneManager
from scene_management.scenes.error import Error
from scene_management.scenes.success import Success

class Login(Scene): 
    do_login: Function(int)

    def __init__(self, master, do_login: Function(int) = None):
        super().__init__(master)
        self.do_login = do_login
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
        id = id.replace("A", "")
        if(id.isdigit()):
            try:
                result = self.do_login(int(id))
                if(result.state is "SUCCESS"):
                    SceneManager.load(Success(self.master, result.message))
                else:
                    SceneManager.load(Error(self.master, result.message))
            except Exception as e:
                SceneManager.load(Error(self.master, e))
        else:
            SceneManager.load(Error(self.master, "このバーコードは使用できません"))
