from PropertyClasses.Parsers.LandParser import LandParser
from PropertyClasses.Parsers.ParserController import MainParser


class PoliticianPropertyParser(MainParser):

    __politician = None
    __landParser = None

    def __init__(self):
        print("Politician Property parse")
        self.__landParser = LandParser()

    def setPolitican(self,politican):
        self.__politician = politican

    def parse(self):
        super().file.seek(self.politician.getPoliticianFilePoisition)
        super().file.readline()


    def checkDivide(self, string):
        print()
