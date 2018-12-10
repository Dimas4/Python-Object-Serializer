from pyserializer.serializer.serializer import BaseSerializer
from pyserializer.field.field_factory.factory import FieldFactory
from example.model.model import Base


class MySerializer(BaseSerializer):
    name = FieldFactory.create('list', min_length=2)
    des = FieldFactory.create('string', min_length=5)
    additional = FieldFactory.create('string')

    def get_additional(self):
        if self['name'] == [1, 2]:
            return 'q'
        return 1


base1 = Base([1, 2], 'qqqqqqq')

base_serializer = MySerializer()

# print(base_serializer.serialize([base1, base1], many=True))
print(base_serializer.serialize(base1))
