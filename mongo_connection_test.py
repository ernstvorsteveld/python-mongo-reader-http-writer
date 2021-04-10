import unittest
from mongo_connection import MongoConnection
import os

class TestMongoConnection(unittest.TestCase):

    def test_should_get_collection_using_default_values(self):
        self.mongo = MongoConnection()
        collection = self.mongo.getCollection('default-collection')
        self.assertEqual(collection.full_name, "default-database-name.default-collection")

    def test_should_get_collection_with_env_variable(self):
        os.environ["MONGO_CONFIG_FILE"] = "mongo-connection-test.json"
        self.mongo = MongoConnection()
        collection = self.mongo.getCollection('test-collection')
        self.assertEqual(collection.full_name, "test-database.test-collection")
        del os.environ["MONGO_CONFIG_FILE"]

    def test_should_get_collection_from_parameter(self):
        self.mongo = MongoConnection("mongo-connection-test.json")
        collection = self.mongo.getCollection('test-collection')
        self.assertEqual(collection.full_name, "test-database.test-collection")
