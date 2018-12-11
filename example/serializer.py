from pyserializer.serializer.serializer import BaseSerializer
from pyserializer.schema.schema import Schema
from example.model.model import Base


def data():
    return 1


class MySerializer(BaseSerializer):
    name = Schema.create('list', min_length=2)
    des = Schema.create('string', min_length=5)
    additional = Schema.create('string')
    func_field = Schema.create('function', func=data)

    def get_additional(self):
        if self['name'] == [1, 2]:
            return 'q'
        return 1


base1 = Base([1, 2], 'qqqqqqq')

base_serializer = MySerializer()

# print(base_serializer.serialize([base1, base1], many=True))
print(base_serializer.serialize(base1))
