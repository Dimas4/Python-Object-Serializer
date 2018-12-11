from pyserializer.field.field_factory.factory import FieldFactory
from .custom_base.sequence import SequenceBase
from .custom_base.function import FunctionBase
from .field_type.funtion import Function
from .base.base import Base


@FieldFactory.registry('function')
class FunctionField(FunctionBase):
    def __init__(self, func):
        super().__init__(Function, func)


@FieldFactory.registry('int')
class IntField(Base):
    def __init__(self):
        super().__init__(int)


@FieldFactory.registry('float')
class FloatField(Base):
    def __init__(self):
        super().__init__(float)


@FieldFactory.registry('string')
class StringField(SequenceBase):
    def __init__(self, max_length=None, min_length=None):
        super().__init__(str, max_length, min_length)


@FieldFactory.registry('tuple')
class TupleField(SequenceBase):
    def __init__(self, max_length=None, min_length=None):
        super().__init__(tuple, max_length, min_length)


@FieldFactory.registry('list')
class ListField(SequenceBase):
    def __init__(self, max_length=None, min_length=None):
        super().__init__(list, max_length, min_length)


@FieldFactory.registry('dict')
class DictField(SequenceBase):
    def __init__(self, max_length=None, min_length=None):
        super().__init__(dict, max_length, min_length)


@FieldFactory.registry('set')
class SetField(SequenceBase):
    def __init__(self, max_length=None, min_length=None):
        super().__init__(set, max_length, min_length)
