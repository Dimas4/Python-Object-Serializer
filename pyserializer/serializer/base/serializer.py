from pyserializer.field.field_type.funtion import Function
from pyserializer.validate.validate import Validate
from abc import ABC, abstractmethod, abstractstaticmethod


class AbstractSerializer(ABC):
    @staticmethod
    @abstractmethod
    def _get_obj_dict(obj):
        """
        Gets obj's attributes
        :param obj:
        :return: obj's attributes
        """
        return obj.__dict__

    @classmethod
    @abstractmethod
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
    @abstractmethod
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
    @abstractmethod
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
    @abstractmethod
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
    @abstractmethod
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
