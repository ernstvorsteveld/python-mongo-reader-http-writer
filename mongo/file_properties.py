import os
import json

class FileProperties:

    def __init__(self, filename=None):
        result = None
        if filename != None:
            result = self.getFilename(filename)
        else:
            try:
                if os.path.exists(os.environ['CONFIG_FILE']):
                    result = self.getFilename(os.environ['CONFIG_FILE'])
            except KeyError:
                self.config = None
                return

        self.config = None
        with open(result) as config_file:
            self.config = json.load(config_file)

    def getFilename(self, filename):        
        return filename if os.path.exists(filename) else None

    def getProperty(self, name):
        if self.config == None:
            return None

        attrs = name.split(".")
        
        sub = self.config
        for attr in attrs:
            sub = sub[attr]
        return sub