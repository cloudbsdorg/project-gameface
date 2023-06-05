import sys
from src.platform.interfaces.keyboard_interface import KeyboardInterface

if sys.platform == "win32":
    import pydirectinput


class WindowsVirtualKeyboard(KeyboardInterface):

    def __init__(self, keymap) -> None:
        # disable lag
        super().__init__(keymap)
        pydirectinput.PAUSE = 0
        pydirectinput.FAILSAFE = False

    def keyDown(self, key):
        action = self.getKey(key)
        if action is not None:
            pydirectinput.keyDown(action)

    def keyUp(self, key):
        action = self.getKey(key)
        if action is not None:
            pydirectinput.keyUp(action)

    def getKey(self, key):
        if key in self.keymap.keys():
            return self.keymap[key]
        return None

