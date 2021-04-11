import requests
import json
import sys

class Sender:

    def __init__(self, inputStream=None):
        self.inputStream = inputStream

    with open("../config.json") as config_file:
        config = json.load(config_file)

    for item in sys.stdin:
        try:
            res = requests.post(config["services"]["inputvalidation-contracts"], json = json.loads(item))
            print(res)
        except requests.exceptions.HTTPError as e:
            print ("something goes wrong with Contract Request: ", e.response.text)