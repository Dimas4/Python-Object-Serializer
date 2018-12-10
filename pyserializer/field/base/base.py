class Base:
    def __init__(self, type, value):
        self.value = value
        self.__type = type

    @property
    def type(self):
        return self.__type
