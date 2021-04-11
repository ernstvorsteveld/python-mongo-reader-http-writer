from mongo.mongo_connection import MongoConnection
from mongo.file_properties import FileProperties

class Reader:
    def __init__(self, start=0, end=None, size=0, configFile=None):
        self.start = start
        self.end = end
        self.size = size
        self.configFile = FileProperties(configFile)

    def run(self):
        self.mongo = MongoConnection(self.configFile)
        collection = self.mongo.getCollection()
        self.end = self.mongo.collectionSize(collection, self.end)
        self.read(collection)

    def read(self, collection):
        limit = min(self.size, self.end)
        skip = self.start
        while skip < self.end:
            documents = collection.find({}).skip(skip).limit(limit)
            for document in documents:
                print(self.mongo.dump(document))
            
            skip = skip + limit
