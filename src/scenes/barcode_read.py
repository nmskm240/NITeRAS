import tkinter as tk
from scenes.scene import Scene
from scenes.scene_manager import SceneManager

class BarcodeRead(Scene): 
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.back = tk.Button(self, text="戻る", command=lambda: SceneManager.back())
        self.back.pack()