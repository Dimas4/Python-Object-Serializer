from pyserializer.serializer.serializer import BaseSerializer
from example.model.model import Base


class MySerializer(BaseSerializer):
    name = str
    des = str


base1 = Base('hi', 'q')

base_serializer = MySerializer()

print(base_serializer.serialize([base1, base1], many=True))
