import unittest
import os
from mongo.file_properties import FileProperties

class TestMongoConnection(unittest.TestCase):

    def test_should_load_correct_file(self):
        self.fileProperties = FileProperties("file_properties_test.json")
        self.assertEqual(self.fileProperties.getProperty("database"), "test_database")
        self.assertEqual(self.fileProperties.getProperty("connect_url"), "mongodb://root:root@127.0.0.1:27017")
        self.assertEqual(self.fileProperties.getProperty("collection"), "test_collection")

    def test_should_load_config_with_env_variable(self):
        os.environ["CONFIG_FILE"] = "file_properties_test.json"
        self.fileProperties = FileProperties()
        self.assertEqual(self.fileProperties.getProperty("database"), "test_database")
        self.assertEqual(self.fileProperties.getProperty("connect_url"), "mongodb://root:root@127.0.0.1:27017")
        self.assertEqual(self.fileProperties.getProperty("collection"), "test_collection")
        del os.environ["CONFIG_FILE"]

