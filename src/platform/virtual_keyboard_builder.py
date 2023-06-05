import sys

from pynput.keyboard import Key

from src.platform import PlatformDetection
from src.platform.interfaces import keyboard_interface

if sys.platform == 'darwin':
    from src.platform.darwin.darwin_virtual_keyboard import DarwinVirtualKeyboard
if sys.platform != 'darwin':
    from src.platform.generic.generic_virtual_keyboard import GenericVirtualKeyboard
if sys.platform == 'win32':
    from src.platform.windows.windows_virtual_keyboard import WindowsVirtualKeyboard


class VirtualKeyboardBuilder(PlatformDetection):
    keymap = {
        # Numbers
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",

        # Functions
        "f1": Key.f1,
        "f2": Key.f2,
        "f3": Key.f3,
        "f4": Key.f4,
        "f5": Key.f5,
        "f6": Key.f6,
        "f7": Key.f7,
        "f8": Key.f8,
        "f9": Key.f9,
        "f10": Key.f10,
        "f11": Key.f11,
        "f12": Key.f12,
        "f13": Key.f13,
        "f14": Key.f14,
        "f15": Key.f15,
        "f16": Key.f16,
        "f17": Key.f17,
        "f18": Key.f18,
        "f19": Key.f19,
        "f20": Key.f20,

        # Letters
        "a": "a",
        "b": "b",
        "c": "c",
        "d": "d",
        "e": "e",
        "f": "f",
        "g": "g",
        "h": "h",
        "i": "i",
        "j": "j",
        "k": "k",
        "l": "l",
        "m": "m",
        "n": "n",
        "o": "o",
        "p": "p",
        "q": "q",
        "r": "r",
        "s": "s",
        "t": "t",
        "u": "u",
        "v": "v",
        "w": "w",
        "x": "x",
        "y": "y",
        "z": "z",

        # Special characters
        "exclam": "!",
        "at": "@",
        "numbersign": "#",
        "dollar": "$",
        "percent": "%",
        "asciicircum": "^",
        "ampersand": "&",
        "asterisk": "*",
        "parenleft": "(",
        "parenright": ")",
        "minus": "-",
        "plus": "+",
        "underscore": "_",
        "equal": "=",
        "bracketleft": "[",
        "bracketright": "]",
        "braceleft": "{",
        "braceright": "}",
        "backslash": "\\",
        "semicolon": ";",
        "colon": ":",
        "apostrophe": "'",
        "quotedbl": "\"",
        "grave": "`",
        "comma": ",",
        "less": "<",
        "greater": ">",
        "question": "?",
        "slash": "/",
        "asciitilde": "~",
        "bar": "|",
        "period": ".",

        # Miscellaneous
        "return": Key.enter,
        "backspace": Key.backspace,
        "tab": Key.tab,
        "space": Key.space,
        "delete": Key.delete,
        "home": Key.home,
        "end": Key.end,
        "next": Key.page_down,
        "prior": Key.page_up,
        "win_l": Key.cmd_l,
        "win_r": Key.cmd_r,
        "caps_lock": Key.caps_lock,
        "shift_l": Key.shift_l,
        "shift_r": Key.shift_r,
        "control_l": Key.ctrl_l,
        "control_r": Key.ctrl_r,
        "alt_l": Key.alt_l,
        "alt_r": Key.alt_r,

        # Directions
        "up": Key.up,
        "down": Key.down,
        "left": Key.left,
        "right": Key.right,
    }

    def __init__(self):
        super().__init__()

    def build(self) -> keyboard_interface:
        if not self.is_darwin():
            self.keymap["num_lock"] = Key.num_lock

        if self.is_windows():
            return WindowsVirtualKeyboard(self.keymap)
        elif self.is_darwin():
            self.keymap["meta_r"] = Key.cmd_r
            self.keymap["meta_l"] = Key.cmd_l
            return DarwinVirtualKeyboard(self.keymap)

        return GenericVirtualKeyboard()
