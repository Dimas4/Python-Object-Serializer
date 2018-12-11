from pyserializer.field.base.base import Base


class FunctionBase(Base):
    def __init__(self, type, func):
        self.func = func
        super().__init__(type)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
