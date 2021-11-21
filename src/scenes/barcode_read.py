import tkinter as tk
from scenes.scene import Scene

class BarcodeRead(Scene): 
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.back = tk.Button(self, text="戻る")
        self.back.pack()