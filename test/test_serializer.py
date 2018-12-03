from pyserializer.serializer.serializer import BaseSerializer


class MySerializerAllFields(BaseSerializer):
    fields = ['name', 'des']


class MySerializerOnlyName(BaseSerializer):
    fields = ['name']


class MySerializerErrorField(BaseSerializer):
    fields = ['name', 'error_field']


serializer_all_fields = MySerializerAllFields()
serializer_only_name = MySerializerOnlyName()
serializer_error_field = MySerializerErrorField()
