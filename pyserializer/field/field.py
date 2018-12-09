class StringField:
    def __init__(self, max_length=None, min_length=None):
        self.__type = str
        self.max_length = max_length
        self.min_length = min_length

    @property
    def type(self):
        return self.__type


class IntField:
    def __init__(self):
        self.__type = int

    @property
    def type(self):
        return self.__type
