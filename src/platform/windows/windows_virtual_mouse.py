import sys

from src.platform.interfaces.mouse_interface import MouseInterface

if sys.platform == "win32":
    import pydirectinput


class WindowsVirtualMouse(MouseInterface):
    mouseButton = {
        "left": pydirectinput.LEFT,
        "middle": pydirectinput.MIDDLE,
        "right": pydirectinput.RIGHT,
        "primary": pydirectinput.PRIMARY,
        "secondary": pydirectinput.SECONDARY
    }

    def destroy(self):
        super().destroy()

    def click(self, button, count=1):
        pydirectinput.click(button=self.mouseButton[button])

    def mouseDown(self, button):
        pydirectinput.mouseDown(button=self.mouseButton[button])

    def mouseUp(self, button):
        pydirectinput.mouseUp(button=self.mouseButton[button])

    def position(self) -> tuple:
        return pydirectinput.position()

    def moveTo(self, x: int, y: int) -> tuple:
        pydirectinput.moveTo(x, y)
