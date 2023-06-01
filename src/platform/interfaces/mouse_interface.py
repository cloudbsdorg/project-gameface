class MouseMeta(type):

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))


class MouseInterface(metaclass=MouseMeta):

    def action(self):
        pass

    def destroy(self):
        pass