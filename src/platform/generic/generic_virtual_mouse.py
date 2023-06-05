from src.platform.interfaces.mouse_interface import MouseInterface
from pynput.mouse import Button, Controller


class GenericVirtualMouse(MouseInterface):
    mouseButton = {
        "left": Button.left,
        "middle": Button.middle,
        "right": Button.right
    }

    def __init__(self) -> None:
        super().__init__()
        self.mouse = Controller()

    def destroy(self):
        super().destroy()

    def click(self, button, count=1):
        self.mouse.click(self.mouseButton[button], count)

    def mouseDown(self, button):
        self.mouse.mouseDown(self.mouseButton[button])

    def mouseUp(self, button):
        self.mouse.mouseUp(self.mouseButton[button])

    def position(self) -> tuple:
        return self.mouse.position

    def moveTo(self, x: int, y: int) -> tuple:
        self.mouse.position = [x, y]
