'''
@Author 최제현
@Date 21/1/8

'''

class Politician:
    __name = None
    __belong = None
    __position = None
    __filePoistion = None
    __fileEndPosition = None
    __Land = None
    __RealEstate = None
    __RealRight = None
    __Deposit = None
    __PoliticDeposit = None
    __Debt = None

    def __init__(self, name, belong, position, filePosition):
        self.__name = name
        self.__belong = belong
        self.__position = position
        self.__filePoistion = filePosition



    @property
    def getLand(self):
        return self.__Land

    @getLand.setter
    def setland(self, Land):
        self.__Land = Land

    @property
    def getPoliticianFilePoisition(self):
        return self.__filePoistion


    @property
    def getPoliticianFileEndPosition(self):
        return self.__fileEndPosition

    @getPoliticianFileEndPosition.setter
    def setPoliticianFileEndPosition(self, pos):
        self.__fileEndPosition = pos

