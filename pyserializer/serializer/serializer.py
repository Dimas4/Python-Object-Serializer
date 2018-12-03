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
    def _get_obj_fields_and_errors(obj, _fields: dict) -> tuple:
        """
        Gets all the specific fields of an obj
        :param obj:
        :param _fields:
        :return: The specific fields of an obj
        """
        _object_field_set = set(obj)
        _obj_wrong_type_fields = set()
        _output = {}

        for key, value in obj.items():
            if key in _fields:
                if not isinstance(value, _fields[key]):
                    _obj_wrong_type_fields.add(key)
                    continue

                _output[key] = value

        _errors_extra_fields = set(_fields) - _object_field_set
        return _output, _errors_extra_fields, _obj_wrong_type_fields

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
    def _add_error_info(cls, _output: dict, _errors_extra_fields: set, _errors_wrong_type_fields: set) -> None:
        """
        Add errors info to _output
        :param _output:
        :param _errors_extra_fields:
        :param _errors_wrong_type_fields:
        :return: _output with errors info
        """
        _output['errors'] = {}
        if _errors_extra_fields:
            _output['errors'].update({'extra_fields': {tuple(_errors_extra_fields): 'Does not exists!'}})
        if _errors_wrong_type_fields:
            _output['errors'].update({'wrong_type': {tuple(_errors_wrong_type_fields): 'Wrong type!'}})

    @classmethod
    def _serialize_many(cls, obj, _fields: dict) -> list:
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
                _data, _errors_extra_fields, _errors_wrong_type_fields = cls._get_obj_fields_and_errors(obj, _fields)
                _output[ind] = _data
                cls._add_error_info(_output[ind], _errors_extra_fields, _errors_wrong_type_fields)
            return _output

    @classmethod
    def _serialize_one(cls, obj, _fields: dict) -> list:
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

        _output, _errors_extra_fields, _errors_wrong_type_fields = cls._get_obj_fields_and_errors(_data, _fields)
        cls._add_error_info(_output, _errors_extra_fields, _errors_wrong_type_fields)
        return _output

    @classmethod
    def serialize(cls, obj, many=False, fields=None) -> list:
        """
        Serializes an obj or array of objs with specific fields
        :param obj:
        :param many:
        :param fields:
        :return: Serialized obj or array of objs
        """

        if fields:
            _fields = set(fields)
        elif len(cls.__dict__) > 2:
            cls_fields = dict(cls.__dict__)
            del cls_fields['__doc__']
            del cls_fields['__module__']

            _fields = cls_fields
        else:
            _fields = None

        if many:
            return cls._serialize_many(obj, _fields)
        return cls._serialize_one(obj, _fields)
