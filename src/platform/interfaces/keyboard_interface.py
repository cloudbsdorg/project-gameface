class KeyboardMeta(type):

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))


class KeyboardInterface(metaclass=KeyboardMeta):

    def __init__(self, keymap) -> None:
        super().__init__()
        self.keymap = keymap

    def get_keymap(self):
        return self.keymap

    def keyDown(self, button):
        pass

    def keyUp(self, button):
        pass
