import tkinter as tk
from scenes.scene import Scene
from scenes.scene_manager import SceneManager

class BarcodeRead(Scene): 
    def on_load(self) -> None:
        self.back = tk.Button(self, text="戻る", command=lambda: SceneManager.back())
        self.back.pack()