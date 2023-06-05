import sys

from src.platform import PlatformDetection
from src.platform.interfaces.display_interface import DisplayInterface
from src.platform.generic.generic_display import GenericDisplay

if sys.platform == 'darwin':
    from src.platform.darwin.darwin_display import DarwinDisplay
if sys.platform == 'win32':
    from src.platform.windows.windows_display import WindowsDisplay


class DisplayBuilder(PlatformDetection):

    def __init__(self):
        super().__init__()

    def build(self) -> DisplayInterface:
        if self.is_windows():
            return WindowsDisplay()
        elif self.is_darwin():
            return DarwinDisplay()
        else:
            return GenericDisplay()
