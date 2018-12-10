from pyserializer.serializer.serializer import BaseSerializer
from pyserializer.field.field_factory.factory import FieldFactory
from example.model.model import Base


class MySerializer(BaseSerializer):
    name = FieldFactory.create('list', min_length=2)
    des = FieldFactory.create('string', min_length=5)
    q = FieldFactory.create('string')
    m = FieldFactory.create('string')

    def get_q(self):
        print(self)
        return 'q'

    def get_m(self):
        print(self)


base1 = Base([1, 2], 'qqqqqqq')

base_serializer = MySerializer()

# print(base_serializer.serialize([base1, base1], many=True))
print(base_serializer.serialize(base1))
