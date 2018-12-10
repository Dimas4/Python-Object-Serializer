from .custom_base.sequence import SequenceBase
from .base.base import Base


@Base.registry('string')
class StringField(Base):
    def __init__(self, max_length=None, min_length=None):
        self.max_length = max_length
        self.min_length = min_length
        super().__init__(str)


@Base.registry('int')
class IntField(Base):
    def __init__(self):
        super().__init__(int)


@Base.registry('tuple')
class TupleField(SequenceBase):
    def __init__(self, max_element_count=None, min_element_count=None):
        super().__init__(tuple, max_element_count, min_element_count)


@Base.registry('list')
class ListField(SequenceBase):
    def __init__(self, max_element_count=None, min_element_count=None):
        super().__init__(list, max_element_count, min_element_count)


@Base.registry('dict')
class DictField(SequenceBase):
    def __init__(self, max_element_count=None, min_element_count=None):
        super().__init__(dict, max_element_count, min_element_count)
