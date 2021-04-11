import unittest
import os
from mongo import MongoConnection
from util import FileProperties

class TestMongoConnection(unittest.TestCase):

    def test_should_get_collection_using_default_values(self):
        self.mongo = MongoConnection(FileProperties(None))
        collection = self.mongo.getCollection()
        self.assertEqual(collection.full_name, "default_database_name.default_collection")

    def test_should_get_collection_from_parameter(self):
        self.mongo = MongoConnection(FileProperties(os.path.dirname(os.path.realpath(__file__)) + "/mongo-connection-test.json"))
        collection = self.mongo.getCollection()
        self.assertEqual(collection.full_name, "test_database.test_collection")
