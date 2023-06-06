class DisplayMeta(type):

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))


class DisplayInterface(metaclass=DisplayMeta):

    def __init__(self):
        self.num_displays = 0
        self.displays = []

    def get_displays(self) -> []:
        return self.displays

    def get_current_display(self, mouse) -> tuple[int, object]:
        x, y = mouse.position()
        for mon_id, mon in enumerate(self.displays):
            if mon["x1"] <= x <= mon["x2"] \
                    and mon["y1"] <= y <= mon["y2"]:
                return [mon_id, mon]
        return 0, None

    def get_current_display_size(self, mouse) -> tuple[int, int]:
        display_id, display = self.get_current_display(mouse)
        return [
            display["x"],
            display["y"]
        ]

    def set_displays(self, display_list):
        self.num_displays = len(display_list)
        i = 0
        for monitor in display_list:
            i += 1
            x = monitor.width
            y = monitor.height
            cur_display = {
                "id": i,
                "x": x,
                "y": y,
                "x1": monitor.x,
                "y1": monitor.y,
                "x2": monitor.x + x,
                "y2": monitor.y + y,
                "center_x": monitor.x + (x // 2),
                "center_y": monitor.y + (y // 2)
            }
            self.displays.append(cur_display)
