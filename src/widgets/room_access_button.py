from scene_management.scene_manager import SceneManager
from scene_management.scenes.login import Login
from utils.misc_helper import MiscHelper
from widgets.image_button import ImageButton
from networks.requests.room_access_data import RoomAccessType

class RoomAccessButton(ImageButton):
    def __init__(self, access_type: RoomAccessType) -> None:
        image_file_name = "login" if access_type == RoomAccessType.IN else "logout"
        super().__init__(image_file_name)
        self.__access_type = access_type

    def _on_click(self) -> None:
        SceneManager.load(Login(self._master, self.__access_type))