from src.platform.interfaces.display_interface import DisplayInterface
from screeninfo import get_monitors


class GenericDisplay(DisplayInterface):

    def __init__(self) -> None:
        super().__init__()
        # monitors need to be sorted, they are out of order from the get_monitors function
        # My primary was not marked as primary, and not in actual order.
        # the Monitor.x attribute led me to be able to properly sort the monitors
        # This still needs to be tested.
        display_list = sorted(get_monitors(), key=lambda display: display.x)
        self.set_displays(display_list)

