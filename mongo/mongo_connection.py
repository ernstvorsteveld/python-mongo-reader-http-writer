import pymongo
import json
import os
import bson.json_util as bj
class MongoConnection:

    def __init__(self, filename=None):
        result = None
        if filename != None:
            result = self.getClientAndDb(filename)
        else:
            if os.path.exists(os.environ['MONGO_CONFIG_FILE']):
                result = self.getClientAndDb(os.environ['MONGO_CONFIG_FILE'])
        
        self.url = "mongodb://root:root@127.0.0.1:27017" if result == None else result[0]
        self.database = "default-database-name" if result == None else result[1]
        self.collection = "default-collection" if result == None else result[2]

        self.client = pymongo.MongoClient(self.url)
        self.db = self.client[self.database]

    def getClientAndDb(self, filename):
        fileToUse = self.getFilename(filename)
        if fileToUse == None:
            return None, None

        with open(fileToUse) as config_file:
            config = json.load(config_file)
            dbName = config["database"]
            dbUrl = config["connect_url"]
            collection = config["collection"]
            return dbUrl, dbName, collection

    def getFilename(self, filename):        
        fileToUse = None
        if os.path.exists(filename):
            fileToUse = filename
        return fileToUse

    def getCollection(self):
        return self.db.get_collection(self.collection)

    def collectionSize(self, collection, end):
        if end == None:
            return collection.count_documents({})
        else:
            return end

    def dump(self, document):
        return bj.dumps(document)

