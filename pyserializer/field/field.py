from .base import Base


class StringField(Base):
    def __init__(self, max_length=None, min_length=None):
        self.max_length = max_length
        self.min_length = min_length
        super().__init__(str)


class IntField(Base):
    def __init__(self):
        super().__init__(int)


class TupleField(Base):
    def __init__(self):
        super().__init__(tuple)


class ListField(Base):
    def __init__(self):
        super().__init__(list)


class DictField:
    def __init__(self):
        super().__init__(dict)
