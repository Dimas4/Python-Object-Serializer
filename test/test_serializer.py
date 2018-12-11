from pyserializer.serializer.base.serializer import BaseSerializer


class MySerializerAllFields(BaseSerializer):
    name = str
    des = str


class MySerializerOnlyName(BaseSerializer):
    name = str


class MySerializerErrorField(BaseSerializer):
    name = str
    error_field = str


class MySerializerWrongType(BaseSerializer):
    name = int
    des = str


class MySerializerWrongTypeExtraField(BaseSerializer):
    name = int
    error_field = str


serializer_all_fields = MySerializerAllFields()
serializer_only_name = MySerializerOnlyName()
serializer_error_field = MySerializerErrorField()
serializer_wrong_type = MySerializerWrongType()
serializer_wrong_type_extra_field = MySerializerWrongTypeExtraField()
