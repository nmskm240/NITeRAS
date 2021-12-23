import tkinter as tk

class ExtensionFunction():
    @classmethod
    def init(cls):
        tk.Misc.root = cls.__get_root_widget

    def __get_root_widget(self) -> tk.Misc:
        node = self
        while not node.master is None:
            node = node.master
        return node