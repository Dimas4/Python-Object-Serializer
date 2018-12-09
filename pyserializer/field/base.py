class Base:
    def __init__(self, type):
        self.__type = type

    @property
    def type(self):
        return self.__type
