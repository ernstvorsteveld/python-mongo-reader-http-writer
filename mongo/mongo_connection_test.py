import unittest
from mongo.mongo_connection import MongoConnection
from mongo.file_properties import FileProperties

class TestMongoConnection(unittest.TestCase):

    def test_should_get_collection_using_default_values(self):
        self.mongo = MongoConnection(FileProperties(None))
        collection = self.mongo.getCollection()
        self.assertEqual(collection.full_name, "default_database_name.default_collection")

    def test_should_get_collection_from_parameter(self):
        self.mongo = MongoConnection(FileProperties("mongo-connection-test.json"))
        collection = self.mongo.getCollection()
        self.assertEqual(collection.full_name, "test_database.test_collection")
