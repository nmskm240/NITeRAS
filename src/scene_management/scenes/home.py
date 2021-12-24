import tkinter as tk

from networks.requests.room_access_data import RoomAccessType
from scene_management.scene import Scene
from widgets.close_button import CloseButton
from widgets.member_button import MemberButton
from widgets.room_access_button import RoomAccessButton
from widgets.setting_button import SettingButton

class Home(Scene) :
    def __init__(self, master):
        super().__init__(master)
        ui = tk.Frame(self)
        access = tk.Frame(ui)
        other = tk.Frame(ui)
        login = RoomAccessButton(
            access,
            RoomAccessType.IN
        )
        logout = RoomAccessButton(
            access, 
            RoomAccessType.OUT
        )
        members = MemberButton(other)
        setting = SettingButton(other)
        members.config(state=tk.DISABLED)
        setting.config(state=tk.DISABLED)
        close = CloseButton(other)
        ui.place(x=0, y=0)
        access.pack(fill=tk.X)
        other.pack(fill=tk.X)
        login.pack(side=tk.LEFT, padx=50, pady=50)
        logout.pack(side=tk.LEFT, padx=50, pady=50)
        setting.pack(side=tk.LEFT, padx=15, pady=15)
        members.pack(side=tk.LEFT, padx=15, pady=15)
        close.pack(side=tk.LEFT, padx=15, pady=15)