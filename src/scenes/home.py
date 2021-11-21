import tkinter as tk
from scenes.barcode_read import BarcodeRead

from scenes.scene import Scene

class Home(Scene) :
    def __init__(self, master= None) -> None:
        super().__init__(master)
        self.room_in = tk.Button(self, text="入室", command= lambda: self.switch(BarcodeRead(master)))
        self.room_out = tk.Button(self, text="退室")
        self.room_in.pack()
        self.room_out.pack()