from pyserializer.serializer.serializer import BaseSerializer
from pyserializer.field.fieldmodel.field import FieldFactory
from example.model.model import Base


class MySerializer(BaseSerializer):
    name = FieldFactory.create('list', min_element_count=5)
    des = FieldFactory.create('string', min_length=5)


base1 = Base([1, 2], 'qqqqqqq')

base_serializer = MySerializer()

# print(base_serializer.serialize([base1, base1], many=True))
print(base_serializer.serialize(base1))
