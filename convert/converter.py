import sys
import os.path
import json
from bson.json_util import dumps

class Converter:

    def __init__(self, inputStream=None):
        self.inputStream = inputStream

    def run(self):
        for item in self.inputStream:
            self.write(self.toJson(item))

    def convertDate(self, collection_item, date):
        if  date is not None:
            year = date.get("year")
            month = date.get("month")
            day = date.get("day")
            return str(year) + "-" + str(month) + "-" + str(day)
        else:
            print("no date is found", collection_item)
            return ""

    def write(self, itemAsJson):
        print(json.dumps(itemAsJson))

    def toJson(self, line):
        return dumps(line)

if __name__ == "__main__":
    Converter(sys.stdin).run()

    