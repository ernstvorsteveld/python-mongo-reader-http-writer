import pymongo
import json
import bson.json_util as bj
import sys
import os
from mongo.file_properties import FileProperties
class MongoConnection:

    def __init__(self, config=None):
        result = self.getClientAndDb(config)
        
        self.url = "mongodb://root:root@127.0.0.1:27017" if result[0] == None else result[0]
        self.database = "default_database_name" if result[1] == None else result[1]
        self.collection = "default_collection" if result[2] == None else result[2]

        self.client = pymongo.MongoClient(self.url)
        self.db = self.client[self.database]

    def getClientAndDb(self, config):
        if config == None:
            return None, None, None

        return config.getProperty("connect_url"), config.getProperty("database"), config.getProperty("collection")

    def getCollection(self):
        return self.db.get_collection(self.collection)

    def collectionSize(self, collection, end):
        if end == None:
            return collection.count_documents({})
        else:
            return end

    def dump(self, document):
        return bj.dumps(document)

