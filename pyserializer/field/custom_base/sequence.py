from pyserializer.field.base.base import Base


class SequenceBase(Base):
    def __init__(self, type, max_element_count=None, min_element_count=None):
        self.max_element_count = max_element_count
        self.min_element_count = min_element_count
        super().__init__(type)
