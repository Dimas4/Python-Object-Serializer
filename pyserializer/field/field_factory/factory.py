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
        _klass = cls._REGISTRY.get(name)
        if not _klass:
            raise NameError
        return _klass(**kwargs)
