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
    def getPoliticianName(self):
        return self.__name

    @property
    def getPoliticianFilePosition(self):
        return self.__filePoistion

    @getPoliticianFilePosition.setter
    def setPoliticianFilePosition(self, pos):
        self.__filePoistion = pos

    @property
    def getPoliticianFileEndPosition(self):
        return self.__fileEndPosition

    @getPoliticianFileEndPosition.setter
    def setPoliticianFileEndPosition(self, pos):
        self.__fileEndPosition = pos

    @property
    def getPoliticianLandProperty(self):
        return self.__Land

    @getPoliticianLandProperty.setter
    def setPoliticianLandProperty(self, land):
        self.__Land = land

    @property
    def getPoliticianRealEstate(self):
        return self.__RealEstate

    @getPoliticianRealEstate.setter
    def setPoliticianRealEstate(self, re):
        self.__RealEstate = re

    @property
    def getPoliticianRealRight(self):
        return self.__RealRight

    @getPoliticianRealRight.setter
    def setPoliticianRealRight(self, rr):
        self.__RealRight = rr

    @property
    def getPoliticianDeposit(self):
        return self.__Deposit

    @getPoliticianDeposit.setter
    def setPoliticianDeposit(self, deposit):
        self.__Deposit = deposit

    @property
    def getPoliticianPoliticDeposit(self):
        return self.__Deposit

    @getPoliticianPoliticDeposit.setter
    def setPoliticianPoliticDeposit(self, deposit):
        self.__PoliticDeposit = deposit


    @property
    def getPoliticianDebt(self):
        return self.__Debt

    @getPoliticianDebt.setter
    def setPoliticianDebt(self, debt):
        self.__Debt = debt
