import tkinter as tk
import os
import requests
from scenes.scene import Scene
from scenes.scene_manager import SceneManager

class BarcodeRead(Scene): 
    def enrollment_check(self) -> None:
        res = requests.get(os.environ["NAME_LIST_API_URL"], { "id": self.entry.get() })
        print(res.text)
        self.result.config(text="非在籍" if res.text == "null" else "在籍")

    def on_load(self) -> None:
        self.entry = tk.Entry(self, name="学籍番号")
        self.result = tk.Label(self)
        self.submit = tk.Button(self, text="送信", command=lambda: self.enrollment_check())
        self.back = tk.Button(self, text="戻る", command=lambda: SceneManager.back())
        self.result.pack()
        self.entry.pack()
        self.submit.pack()
        self.back.pack()