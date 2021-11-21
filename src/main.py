import tkinter as tk

from scenes.home import Home

app = tk.Tk()
app.state("zoom")
app.resizable(False, False)
app.title("NITeRAS")

home = Home(app)
home.load()

app.mainloop()