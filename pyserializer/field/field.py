from .custom_base.sequence import SequenceBase
from pyserializer.field.field_factory.factory import FieldFactory
from .base.base import Base


@FieldFactory.registry('int')
class IntField(Base):
    def __init__(self, value):
        super().__init__(int, value)


@FieldFactory.registry('float')
class FloatField(Base):
    def __init__(self, value):
        super().__init__(float, value)


@FieldFactory.registry('string')
class StringField(SequenceBase):
    def __init__(self, value, max_length=None, min_length=None):
        super().__init__(str, value, max_length, min_length)


@FieldFactory.registry('tuple')
class TupleField(SequenceBase):
    def __init__(self, value, max_length=None, min_length=None):
        super().__init__(tuple, value, max_length, min_length)


@FieldFactory.registry('list')
class ListField(SequenceBase):
    def __init__(self, value, max_length=None, min_length=None):
        super().__init__(list, value, max_length, min_length)


@FieldFactory.registry('dict')
class DictField(SequenceBase):
    def __init__(self, value, max_length=None, min_length=None):
        super().__init__(dict, value, max_length, min_length)


@FieldFactory.registry('set')
class SetField(SequenceBase):
    def __init__(self, value, max_length=None, min_length=None):
        super().__init__(set, value, max_length, min_length)
