from pyserializer.exception.exception import ManyError
from .base.serializer import AbstractSerializer
from pyserializer.field import field


class BaseSerializer(AbstractSerializer):
    @classmethod
    def _get_obj_dict(cls, obj):
        return super()._get_obj_dict(obj)

    @classmethod
    def _add_func_type_field(cls, _fields: dict, _field: str, _output: dict) -> bool or None:
        return super()._add_func_type_field(_fields, _field, _output)

    @classmethod
    def _get_extra_field_with_func(cls, _output: dict, _fields: dict, _errors_extra_fields: set) -> None:
        return super()._get_extra_field_with_func(_output, _fields, _errors_extra_fields)

    @classmethod
    def _get_obj_fields_and_errors(cls, obj, _fields: dict) -> tuple:
        return super()._get_obj_fields_and_errors(obj, _fields)

    @classmethod
    def _is_iter(cls, obj) -> bool:
        return super()._is_iter(obj)

    @classmethod
    def _add_error_info(cls, _output: dict, **kwargs) -> None:
        return super()._add_error_info(_output, **kwargs)


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
