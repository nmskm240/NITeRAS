import tkinter as tk

from abc import ABCMeta, abstractmethod

from utils.config import Config

class ImageButton(tk.Button, metaclass=ABCMeta):
    def __init__(self, master, image_file_name: str) -> None:
        image_path = f"../resources/{Config().layout}/images/widgets/{image_file_name}.png"
        image = tk.PhotoImage(file=image_path)
        super().__init__(
            master,
            command = lambda: self._on_click(),
            image = image,
            background=None
        )
        self.image = image

    @abstractmethod
    def _on_click(self) -> None:
        pass