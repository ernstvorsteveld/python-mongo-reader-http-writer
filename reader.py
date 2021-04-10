import argparse
from mongo.mongo_connection import MongoConnection

class Reader:
    def __init__(self, start=0, end=None, size=0, configFile=None):
        self.start = start
        self.end = end
        self.size = size
        self.configFile = configFile

    def run(self):
        mongo = MongoConnection(self.configFile)
        collection = mongo.getCollection()
        self.end = mongo.collectionSize(collection, self.end)
        self.read(collection)

    def read(self, collection):
        limit = min(self.size, self.end)
        skip = self.start
        while skip < self.end:
            documents = collection.find({}).skip(skip).limit(limit)
            for document in documents:
                print(document)
            
            skip = skip + limit



if __name__ == "__main__":    
    parser = argparse.ArgumentParser(description='Reader of MongoDB documents.')

    parser.add_argument('--start', action='store', type=int, default=0,
                    help='The document number to start with (default 0)')
    parser.add_argument('--end', action='store', type=int,
                    help='The document number to end with (default last)')
    parser.add_argument('--size', action='store', type=int, default=10,
                    help='The document count to handle (default 10)')
    parser.add_argument('--config', action='store', type=str,
                    help='The configuration file to use.')
    args = parser.parse_args()
    Reader(args.start, args.end, args.size, args.config).run()
