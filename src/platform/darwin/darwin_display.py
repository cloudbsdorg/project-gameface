from src.platform.interfaces.display_interface import DisplayInterface
from screeninfo import get_monitors, Enumerator, Monitor


class DarwinDisplay(DisplayInterface):

    def __init__(self) -> None:
        super().__init__()
        # monitors need to be sorted, they are out of order from the get_monitors function
        # My primary was not marked as primary, and not in actual order.
        # the Monitor.x attribute led me to be able to properly sort the monitors
        display_list = sorted(get_monitors(Enumerator.OSX), key=lambda display: display.x)
        self.set_displays(display_list)
