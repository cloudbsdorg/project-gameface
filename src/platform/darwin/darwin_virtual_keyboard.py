from src.platform.interfaces.keyboard_interface import KeyboardInterface
from pynput.keyboard import Key, Controller


class DarwinVirtualKeyboard(KeyboardInterface):

    def __init__(self, keymap) -> None:
        super().__init__(keymap)
        self.keyboard = Controller()

    def keyDown(self, key):
        action = self.getKey(key)
        if action is not None:
            self.keyboard.press(action)

    def keyUp(self, key):
        action = self.getKey(key)
        if action is not None:
            self.keyboard.release(action)

    def getKey(self, key):
        if key in self.keymap.keys():
            return self.keymap[key]
        return None
