import tkinter as tk
import platform

from dotenv import load_dotenv
load_dotenv()

from scene_management.scenes.home import Home
from scene_management.scene_manager import SceneManager

app = tk.Tk()
if platform.system() == "Windows":
    app.state("zoom")
else:
    app.attributes("-zoomed", True)
app.resizable(False, False)
app.title("NITeRAS")

SceneManager.load(Home(app))

app.mainloop()