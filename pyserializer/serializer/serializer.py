from pyserializer.exception.exception import ManyError


class BaseSerializer:
    @staticmethod
    def _get_obj_dict(obj):
        """
        Gets obj's attributes
        :param obj:
        :return: obj's attributes
        """
        return obj.__dict__

    @staticmethod
    def _get_dict_by_field(obj, _fields: set) -> tuple:
        """
        Gets all the specific fields of an obj
        :param obj:
        :param _fields:
        :return: The specific fields of an obj
        """
        _errors_fields_set = set()
        _output = {}
        for key, value in obj.items():
            if key in _fields:
                _errors_fields_set.add(key)
                _output[key] = value

        _errors = _fields - _errors_fields_set
        return _output, _errors

    @staticmethod
    def _is_iter(obj) -> bool:
        """
        Checks if the obj is iterable
        :param obj:
        :return: True if obj is iterable, else False
        """
        try:
            iter(obj)
            return True
        except TypeError:
            return False

    @classmethod
    def _add_not_exists_error_info(cls, _output, _errors, many):
        """
        Add errors info to _output
        :param _output:
        :param _errors:
        :param many:
        :return: _output with errors info
        """
        if many:
            _output.append({'errors': {tuple(_errors): 'Does not exists!'} if _errors else ''})
        else:
            _output.update({'errors': {tuple(_errors): 'Does not exists!'} if _errors else ''})

    @classmethod
    def _serialize_many(cls, obj, _fields: set) -> list:
        """
        Serializes array of objs
        :param obj:
        :param _fields:
        :return: Array of serialized objs
        """
        _data = []

        if not cls._is_iter(obj):
            raise ManyError

        for obj in obj:
            _data.append(cls._get_obj_dict(obj))

        if _fields:
            _output = []
            for ind, obj in enumerate(_data):
                _output.append({})
                _data, _errors = cls._get_dict_by_field(obj, _fields)
                _output[ind] = _data

            cls._add_not_exists_error_info(_output, _errors, many=True)
            return _output

    @classmethod
    def _serialize_one(cls, obj, _fields: set) -> dict:
        """
        Serializes one obj
        :param obj:
        :param _fields:
        :return: Serialized objs
        """
        try:
            _data = cls._get_obj_dict(obj)
        except AttributeError:
            raise ManyError

        if _fields:
            _output, _errors = cls._get_dict_by_field(_data, _fields)
            cls._add_not_exists_error_info(_output, _errors, many=False)
            return _output
        return _data

    @classmethod
    def serialize(cls, obj, many=False, fields=None) -> list:
        """
        Serializes an obj or array of objs with specific fields
        :param obj:
        :param many:
        :param fields:
        :return: Serialized obj or array of objs
        """

        _fields = set(fields) if fields else (set(cls.fields) if cls.fields else None)

        if many:
            return cls._serialize_many(obj, _fields)
        return [cls._serialize_one(obj, _fields)]
