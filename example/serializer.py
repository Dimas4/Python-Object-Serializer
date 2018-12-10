from pyserializer.serializer.serializer import BaseSerializer
from pyserializer.field.base.base import Base as BaseModel
from pyserializer.field import field
from example.model.model import Base


model = BaseModel.create('string', min_length=5)


class MySerializer(BaseSerializer):
    name = BaseModel.create('list', min_element_count=2)
    des = BaseModel.create('string', min_length=5)


base1 = Base([1, 2], 'qqqqqqq')

base_serializer = MySerializer()

# print(base_serializer.serialize([base1, base1], many=True))
print(base_serializer.serialize(base1))
