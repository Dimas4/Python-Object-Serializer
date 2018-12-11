from abc import ABC, abstractmethod


class AbstractSerializer(ABC):
    @staticmethod
    @abstractmethod
    def _get_obj_dict(obj): ...

    @staticmethod
    @abstractmethod
    def _is_iter(obj) -> bool: ...

    @classmethod
    @abstractmethod
    def _add_func_type_field(cls, _fields: dict, _field: str, _output: dict) -> bool or None: ...

    @classmethod
    @abstractmethod
    def _get_extra_field_with_func(cls, _output: dict, _fields: dict, _errors_extra_fields: set) -> None: ...

    @classmethod
    @abstractmethod
    def _get_obj_fields_and_errors(cls, obj, _fields: dict) -> tuple: ...

    @classmethod
    @abstractmethod
    def _add_error_info(cls, _output: dict, **kwargs) -> None:  ...

    @classmethod
    @abstractmethod
    def _serialize_many(cls, obj, _fields: dict) -> list: ...

    @classmethod
    @abstractmethod
    def _serialize_one(cls, obj, _fields: dict) -> list: ...

    @classmethod
    @abstractmethod
    def serialize(cls, obj, many=False, fields=None) -> list: ...
