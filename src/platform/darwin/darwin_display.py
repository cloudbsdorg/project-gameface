from src.platform.interfaces.display_interface import DisplayInterface
from screeninfo import get_monitors, Enumerator, Monitor


class DarwinDisplay(DisplayInterface):

    def __init__(self) -> None:
        super().__init__()
        i = 0
        prevmonitor = None
        # monitors need to be sorted, they are out of order from the get_monitors function
        # My primary was not marked as primary, and not in actual order.
        # the Monitor.x attribute led me to be able to properly sort the monitors
        # MacOS may need the Enumerator.OSX on some installs, adding as per documentation to be safe
        display_list = sorted(get_monitors(Enumerator.OSX), key=lambda display: display.x)
        self.num_displays = len(display_list)
        prevXend = 0
        for monitor in display_list:
            i += 1
            if prevmonitor is not None:
                prevXend += prevmonitor.width
            xStart = prevXend
            yStart = 0
            x = monitor.width
            y = monitor.height
            xEnd = xStart + x
            yEnd = monitor.height
            cur_display = {
                "id": i,
                "x": x,
                "y": y,
                "x1": xStart,
                "y1": yStart,
                "x2": xEnd,
                "y2": yEnd,
                "center_x": (xStart + xEnd) // 2,
                "center_y": (yStart + yEnd) // 2
            }
            prevmonitor = monitor
            self.displays.append(cur_display)


