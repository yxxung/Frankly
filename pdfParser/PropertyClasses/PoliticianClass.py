'''
@Author 최제현
@Date 21/1/8

'''

class Politician:
    # name = None
    # belong = None
    # position = None
    # filePoistion = None
    # fileEndPosition = None
    # Land = None
    # RealEstate = None
    # RealRight = None
    # Deposit = None
    # PoliticDeposit = None
    # Debt = None
    # propertyChangeList = None



    def __init__(self, name, belong, position, filePosition):
        self.name = name
        self.belong = belong
        self.position = position
        self.filePosition = filePosition

    @property
    def getName(self):
        return self.name
    @getName.setter
    def setName(self, name):
        self.name = name
    @property
    def getFilePosition(self):
        return self.filePosition

    @getFilePosition.setter
    def setFilePosition(self, pos):
        self.filePosition = pos

    @property
    def getFileEndPosition(self):
        return self.fileEndPosition

    @getFileEndPosition.setter
    def setFileEndPosition(self, pos):
        self.fileEndPosition = pos

    @property
    def getLandProperty(self):
        return self.Land

    @getLandProperty.setter
    def setLandProperty(self, land):
        self.Land = land

    @property
    def getRealEstate(self):
        return self.RealEstate

    @getRealEstate.setter
    def setRealEstate(self, re):
        self.RealEstate = re

    @property
    def getRealRight(self):
        return self.RealRight

    @getRealRight.setter
    def setRealRight(self, rr):
        self.RealRight = rr

    @property
    def getDeposit(self):
        return self.Deposit

    @getDeposit.setter
    def setDeposit(self, deposit):
        self.Deposit = deposit

    @property
    def getPoliticDeposit(self):
        return self.Deposit

    @getPoliticDeposit.setter
    def setPoliticDeposit(self, deposit):
        self.PoliticDeposit = deposit


    @property
    def getDebt(self):
        return self.Debt

    @getDebt.setter
    def setDebt(self, debt):
        self.Debt = debt

    @property
    def getPoliticianPropertyChangeList(self):
        return self.politicianPropertyChangeList


    @getPoliticianPropertyChangeList.setter
    def setPoliticianPropertyChangeList(self, propertyChange):
        self.politicianPropertyChangeList = propertyChange

    @property
    def getPoliticianPropertyChangeDetailList(self):
        return self.politicianPropertyChangeDetailList


    @getPoliticianPropertyChangeDetailList.setter
    def setPoliticianPropertyChangeDetailList(self, propertyChange):
        self.politicianPropertyChangeDetailList = propertyChange