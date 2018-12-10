class Base:
    _REGISTRY = {}

    def __init__(self, type):
        self.__type = type

    @classmethod
    def registry(cls, name):
        def decorator(klass):
            cls._REGISTRY[name] = klass
            return klass
        return decorator

    @classmethod
    def create(cls, name, **kwargs):
        klass = cls._REGISTRY[name]
        if not klass:
            raise NameError
        return klass(**kwargs)

    @property
    def type(self):
        return self.__type
