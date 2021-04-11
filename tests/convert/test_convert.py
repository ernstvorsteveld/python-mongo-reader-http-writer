import unittest
from convert import Converter
import json

class TestConverter(unittest.TestCase):

    def test_should_convert(self):
        input = '{"_id": {"$oid": "607164b5c7846b9a1e3af89e"}, "x": 1.0}'
        converter = Converter()
        itemAsJson = converter.toJson(input)
        converter.write(itemAsJson)
        self.assertEqual(itemAsJson['x'], 1.0)
