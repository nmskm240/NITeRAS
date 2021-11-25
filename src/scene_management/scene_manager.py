import warnings
from scene_management.scene import Scene

class SceneManager():
    __stack: list[Scene] = list()
    __currentScene: Scene = None

    def __init__(self) -> None:
        pass

    @classmethod
    def load(cls, scene: Scene) -> None:
        if(cls.__currentScene is not None):
            cls.__stack.append(cls.__currentScene)
            cls.__currentScene.pack_forget()
            cls.__currentScene.on_hide()
        cls.__currentScene = scene
        scene.pack()

    @classmethod
    def back(cls) -> None:
        if(cls.__stack.count == 0):
            warnings.warn("can't go back any further.")
            return
        scene = cls.__stack.pop()
        cls.__currentScene.destroy()
        cls.__currentScene = scene
        scene.pack()
        scene.on_show()