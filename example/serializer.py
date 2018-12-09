from pyserializer.serializer.serializer import BaseSerializer
from pyserializer.field import field
from example.model.model import Base


class MySerializer(BaseSerializer):
    name = field.StringField(max_length=50)
    des = field.StringField(min_length=5)


base1 = Base('haaaaaaaaaaaaaaaai', 'qqq')

base_serializer = MySerializer()

# print(base_serializer.serialize([base1, base1], many=True))
print(base_serializer.serialize(base1))
