import sys

from src.platform.detection.platform_detection import PlatformDetection
if sys.platform == "win32":
    import pydirectinput
    import win32api
    import ctypes


class FontManagement(PlatformDetection):

    def add_font_resource(self, font_file: str) -> None:
        if self.is_windows():
            gdi32 = ctypes.WinDLL('gdi32')
            gdi32.AddFontResourceW(font_file)

    def remove_font_resource(self, font_file: str) -> None:
        if self.is_windows():
            gdi32 = ctypes.WinDLL('gdi32')
            gdi32.RemoveFontResourceW(font_file)
