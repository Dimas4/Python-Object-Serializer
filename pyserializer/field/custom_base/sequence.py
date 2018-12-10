from pyserializer.field.base.base import Base


class SequenceBase(Base):
    def __init__(self, type, value, max_length=None, min_length=None):
        self.max_length = max_length
        self.min_length = min_length
        super().__init__(type, value)
