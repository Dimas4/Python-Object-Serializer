from .custom_base.sequence import SequenceBase
from .fieldmodel.field import FieldFactory
from .base.base import Base


@FieldFactory.registry('string')
class StringField(Base):
    def __init__(self, max_length=None, min_length=None):
        self.max_length = max_length
        self.min_length = min_length
        super().__init__(str)


@FieldFactory.registry('int')
class IntField(Base):
    def __init__(self):
        super().__init__(int)


@FieldFactory.registry('tuple')
class TupleField(SequenceBase):
    def __init__(self, max_element_count=None, min_element_count=None):
        super().__init__(tuple, max_element_count, min_element_count)


@FieldFactory.registry('list')
class ListField(SequenceBase):
    def __init__(self, max_element_count=None, min_element_count=None):
        super().__init__(list, max_element_count, min_element_count)


@FieldFactory.registry('dict')
class DictField(SequenceBase):
    def __init__(self, max_element_count=None, min_element_count=None):
        super().__init__(dict, max_element_count, min_element_count)
