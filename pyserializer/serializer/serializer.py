from pyserializer.field.field_type.funtion import Function
from pyserializer.exception.exception import ManyError
from pyserializer.validate.validate import Validate
from .base.serializer import AbstractSerializer
from pyserializer.field import field


class BaseSerializer(AbstractSerializer):
    @staticmethod
    def _get_obj_dict(obj):
        """
        Gets obj's attributes
        :param obj:
        :return: obj's attributes
        """
        return obj.__dict__

    @classmethod
    def _add_func_type_field(cls, _fields: dict, _field: str, _output: dict) -> bool or None:
        try:
            if _fields[_field].type is Function:
                if callable(_fields[_field]):
                    _output[_field] = _fields[_field]()
                elif hasattr(_fields[_field], 'func'):
                    _output[_field] = _fields[_field].func()
                else:
                    _output[_field] = None
                return True
        except AttributeError:
            pass

    @classmethod
    def _get_extra_field_with_func(cls, _output: dict, _fields: dict, _errors_extra_fields: set) -> None:
        """
        Adds func type to _output
        :param _output:
        :param _fields:
        :param _errors_extra_fields:
        :return: _output
        """
        _prepared = dict(_output)

        for _field in set(_errors_extra_fields):
            if _field.startswith('get_'):
                _errors_extra_fields.remove(_field)

            _get_field_func = _fields.get(f'get_{_field}')
            if _get_field_func:
                _errors_extra_fields.remove(_field)
                _output[_field] = _get_field_func(_prepared)
                continue

            if cls._add_func_type_field(_fields, _field, _output):
                _errors_extra_fields.remove(_field)

    @classmethod
    def _get_obj_fields_and_errors(cls, obj, _fields: dict) -> tuple:
        """
        Gets all the specific fields of an obj
        :param obj:
        :param _fields:
        :return: The specific fields of an obj
        """
        _object_field_set = set(obj)
        _obj_wrong_type_fields = set()
        _obj_wrong_params_field = [{} for _ in range(len(obj))]
        _output = {}

        for ind, (_key, _value) in enumerate(obj.items()):
            if _key in _fields:
                if not isinstance(_fields[_key].type, type) or not isinstance(_value, _fields[_key].type):
                    _obj_wrong_type_fields.add(_key)
                    continue

                _validate_errors = Validate.validate_errors(_fields[_key], _value)
                for _error in _validate_errors:
                    _obj_wrong_params_field[ind].update(_error)

                _output[_key] = _value

        _errors_extra_fields = set(_fields) - _object_field_set

        cls._get_extra_field_with_func(_output, _fields, _errors_extra_fields)

        return _output, _errors_extra_fields, _obj_wrong_type_fields, _obj_wrong_params_field

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
    def _add_error_info(cls, _output: dict, **kwargs) -> None:
        """
        Add errors info to _output
        :param _output:
        :param _errors_extra_fields:
        :param _errors_wrong_type_fields:
        :return: _output with errors info
        """
        _output['errors'] = {}
        for key, value in kwargs.items():
            if isinstance(value, list):
                for ind, element in enumerate(value):
                    if element:
                        _output['errors'].update({list(_output.items())[ind][0]: dict(element.items())})
                continue
            if value:
                _output['errors'].update({key: list(value)})

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
                _data, _errors_extra_fields, _errors_wrong_type_fields, _obj_wrong_params_field = \
                    cls._get_obj_fields_and_errors(obj, _fields)

                _output[ind] = _data
                cls._add_error_info(_output[ind], extra_fields=_errors_extra_fields,
                                    wrong_type=_errors_wrong_type_fields,
                                    wrong_additional_params=_obj_wrong_params_field)
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

        _output, _errors_extra_fields, _errors_wrong_type_fields, _obj_wrong_params_field = \
            cls._get_obj_fields_and_errors(_data, _fields)
        cls._add_error_info(_output, extra_fields=_errors_extra_fields,
                            wrong_type=_errors_wrong_type_fields,
                            wrong_additional_params=_obj_wrong_params_field)

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
            _fields = {}
            for _field in fields:
                _fields[_field] = dict(cls.__dict__)[_field]
        elif len(cls.__dict__) > 2:
            cls_fields = dict(cls.__dict__)
            _extra_fields = ['__doc__', '__module__', '_abc_cache', '_abc_negative_cache',
                             '_abc_negative_cache_version', '__abstractmethods__', '_abc_registry']
            for _extra_field in _extra_fields:
                del cls_fields[_extra_field]

            _fields = cls_fields
        else:
            _fields = None
        if many:
            return cls._serialize_many(obj, _fields)
        return cls._serialize_one(obj, _fields)
