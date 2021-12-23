import tkinter as tk
from abc import ABCMeta, abstractmethod

class ImageButton(tk.Button, metaclass=ABCMeta):
    def __init__(self, master, image) -> None:
        super().__init__(
            master,
            command=lambda: self._on_click(),
            image=image,
        )
        self.image = image

    @abstractmethod
    def _on_click(self) -> None:
        pass