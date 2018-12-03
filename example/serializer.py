from pyserializer.serializer.serializer import BaseSerializer
from example.model.model import Base


class MySerializer(BaseSerializer):
    fields = ['name', 'des']


base1 = Base('hi', 'q')
base2 = Base('h', 'z')
base3 = Base('f', 'v')

base_serializer = MySerializer()

print(base_serializer.serialize(base1))
print(base_serializer.serialize(base1, fields=['name']))
print(base_serializer.serialize([base1, base2], many=True))
print(base_serializer.serialize([base1, base2], many=True, fields=['des']))
