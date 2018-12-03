import unittest

from pyserializer.exception.exception import ManyError

from test_serializer import (
    serializer_all_fields,
    serializer_only_name,
    serializer_error_field,
    serializer_wrong_type,
    serializer_wrong_type_extra_field
)

from test_model import Base


class TestSerializer(unittest.TestCase):
    def setUp(self):
        self.base = Base('name', 'des')

    def test_one_all_fields(self):
        data = serializer_all_fields.serialize(self.base)
        self.assertEqual(data, {'name': 'name', 'des': 'des', 'errors': {}})

    def test_many_all_fields(self):
        data = serializer_all_fields.serialize([self.base, self.base], many=True)
        self.assertEqual(data, [{'name': 'name', 'des': 'des', 'errors': {}}, {'name': 'name', 'des': 'des', 'errors': {}}])

    def test_one_all_fields_error_many(self):
        with self.assertRaises(ManyError):
            serializer_all_fields.serialize(self.base, many=True)

    def test_many_all_fields_error_many(self):
        with self.assertRaises(ManyError):
            serializer_all_fields.serialize([self.base, self.base])

    def test_one_only_name(self):
        data = serializer_only_name.serialize(self.base)
        self.assertEqual(data, {'name': 'name', 'errors': {}})

    def test_many_only_name(self):
        data = serializer_only_name.serialize([self.base, self.base], many=True)
        self.assertEqual(data, [{'name': 'name', 'errors': {}}, {'name': 'name', 'errors': {}}])

    def test_one_only_name_error_many(self):
        with self.assertRaises(ManyError):
            serializer_only_name.serialize(self.base, many=True)

    def test_many_only_name_error_many(self):
        with self.assertRaises(ManyError):
            serializer_only_name.serialize([self.base, self.base])

    def test_one_error_field(self):
        data = serializer_error_field.serialize(self.base)
        self.assertEqual(data, {'name': 'name', 'errors': {'extra_fields': {('error_field',): 'Does not exists!'}}})

    def test_many_error_field(self):
        data = serializer_error_field.serialize([self.base, self.base], many=True)
        self.assertEqual(data, [{'name': 'name', 'errors': {'extra_fields': {('error_field',): 'Does not exists!'}}},
                                {'name': 'name', 'errors': {'extra_fields': {('error_field',): 'Does not exists!'}}}])

    def test_one_wrong_type(self):
        data = serializer_wrong_type.serialize(self.base)
        self.assertEqual(data, {'des': 'des', 'errors': {'wrong_type': {('name',): 'Wrong type!'}}})

    def test_many_wrong_type(self):
        data = serializer_wrong_type.serialize([self.base, self.base], many=True)
        self.assertEqual(data, [{'des': 'des', 'errors': {'wrong_type': {('name',): 'Wrong type!'}}},
                                {'des': 'des', 'errors': {'wrong_type': {('name',): 'Wrong type!'}}}])

    def test_one_wrong_type_extra_field(self):
        data = serializer_wrong_type_extra_field.serialize(self.base)
        self.assertEqual(data, {'errors': {'extra_fields': {('error_field',): 'Does not exists!'},
                                           'wrong_type': {('name',): 'Wrong type!'}}})

    def test_many_wrong_type_extra_field(self):
        data = serializer_wrong_type_extra_field.serialize([self.base, self.base], many=True)
        self.assertEqual(data, [{'errors': {'extra_fields': {('error_field',): 'Does not exists!'},
                                            'wrong_type': {('name',): 'Wrong type!'}}},
                                {'errors': {'extra_fields': {('error_field',): 'Does not exists!'},
                                            'wrong_type': {('name',): 'Wrong type!'}}}])


if __name__ == '__main__':
    unittest.main()
