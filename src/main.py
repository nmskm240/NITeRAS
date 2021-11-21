import tkinter as tk

from dotenv import load_dotenv

from scenes.home import Home
from scenes.scene_manager import SceneManager

load_dotenv()

app = tk.Tk()
app.state("zoom")
app.resizable(False, False)
app.title("NITeRAS")

SceneManager.load(Home(app))

app.mainloop()