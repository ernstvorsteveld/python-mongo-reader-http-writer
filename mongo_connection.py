from pymongo import MongoClient
import json
import os.path
from os import path
import os
class MongoConnection:

    def __init__(self, filename=None):
        result = None
        if filename != None:
            result = self.getClientAndDb(filename)
        else:
            if path.exists(os.environ['MONGO_CONFIG_FILE']):
                print("env", os.environ['MONGO_CONFIG_FILE'])
                result = self.getClientAndDb(os.environ['MONGO_CONFIG_FILE'])
        
        self.url = "mongodb://root:root@127.0.0.1:27017" if result == None else result[0]
        self.database = "default-database-name" if result == None else result[1]

        self.client = MongoClient(self.url)
        self.db = self.client[self.database]

    def getClientAndDb(self, filename):
        fileToUse = self.getFilename(filename)
        if fileToUse == None:
            return None, None

        with open(fileToUse) as config_file:
            config = json.load(config_file)
            dbName = config["database"]
            dbUrl = config["connect_url"]
            return dbUrl, dbName

    def getFilename(self, filename):        
        fileToUse = None
        if path.exists(filename):
            fileToUse = filename
        return fileToUse

    def getCollection(self, name):
        return self.db.get_collection(name)