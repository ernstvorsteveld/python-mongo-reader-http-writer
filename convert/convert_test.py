import unittest
from converter import Converter
import json

class TestConverter(unittest.TestCase):

    def test_should_convert(self):
        input = '{"_id": {"$oid": "607164b5c7846b9a1e3af89e"}, "x": 1.0}'
        itemAsJson = json.loads(input)
        print(itemAsJson)
        self.assertEqual(itemAsJson['x'], 1.0)
