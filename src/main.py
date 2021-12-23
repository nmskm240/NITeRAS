import tkinter as tk
import platform

from dotenv import load_dotenv

from utils.extension_function import ExtensionFunction
load_dotenv()

from scene_management.scenes.home import Home
from scene_management.scene_manager import SceneManager

app = tk.Tk()
if platform.system() == "Windows":
    app.geometry("1024x600")
else:
    app.attributes("-zoomed", True)
app.resizable(False, False)
app.title("NITeRAS")

ExtensionFunction.init()
SceneManager.load(Home(app))

app.mainloop()