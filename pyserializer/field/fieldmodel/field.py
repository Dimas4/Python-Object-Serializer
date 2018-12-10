class FieldFactory:
    _REGISTRY = {}

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