import json

class Configs:
    def __init__(self):
        imagesPath : str

    def update(self,configsFilePath : str):
        with open((configsFilePath),'r') as file:
            configs = json.load(file)
            self.imagesPath = configs['images']
            self.bigMage = self.imagesPath['bigMage']
            self.rightSmallMage = self.imagesPath["rightSmallMage"]
            self.smallMage = self.imagesPath["smallMage"]