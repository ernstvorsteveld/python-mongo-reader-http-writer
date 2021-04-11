import unittest
import os, sys
from util import FileProperties

class TestMongoConnection(unittest.TestCase):

    def test_should_load_correct_file(self):
        self.fileProperties = FileProperties(self.getCompletePath("/file_properties_test.json"))
        self.assertEqual(self.fileProperties.getProperty("database"), "test_database")
        self.assertEqual(self.fileProperties.getProperty("connect_url"), "mongodb://root:root@127.0.0.1:27017")
        self.assertEqual(self.fileProperties.getProperty("collection"), "test_collection")

    def test_should_load_config_with_env_variable(self):
        os.environ["CONFIG_FILE"] = self.getCompletePath("/file_properties_test.json")
        self.fileProperties = FileProperties()
        self.assertEqual(self.fileProperties.getProperty("database"), "test_database")
        self.assertEqual(self.fileProperties.getProperty("connect_url"), "mongodb://root:root@127.0.0.1:27017")
        self.assertEqual(self.fileProperties.getProperty("collection"), "test_collection")
        del os.environ["CONFIG_FILE"]

    def getCompletePath(self, filename):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return dir_path + filename


