import tkinter as tk
import os
import requests
from networks.requests.StudentID import StudentID
from networks.responses.DiscordData import DiscordData
from networks.responses.Game import Game
from networks.responses.MemberData import MemberData
from scenes.scene import Scene
from scenes.scene_manager import SceneManager

class Login(Scene): 
    def enrollment_check(self) -> None:
        dto = StudentID(int(self.entry.get()))
        res = requests.get(os.environ["NAME_LIST_API_URL"], dto.to_dict())
        print(MemberData.from_json(res.text))
        self.result.config(text="非在籍" if res.text == "null" else "在籍")

    def on_load(self) -> None:
        self.entry = tk.Entry(self)
        self.result = tk.Label(self)
        self.submit = tk.Button(self, text="送信", command=lambda: self.enrollment_check())
        self.back = tk.Button(self, text="戻る", command=lambda: SceneManager.back())
        self.result.pack()
        self.entry.pack()
        self.submit.pack()
        self.back.pack()