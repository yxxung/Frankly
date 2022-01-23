from PropertyClasses.DebtClass import Debt
from PropertyClasses.DepositClass import Deposit
from PropertyClasses.LandPropertyClass import LandProperty
from PropertyClasses.Parsers.Land import LandParser
from PropertyClasses.PoliticDepositClass import PoliticDeposit
from PropertyClasses.RealEstateClass import RealEstate
from PropertyClasses.RealRightClass import RealRight


class PoliticianPropertyParser():
    __file = None
    __filePos = 0
    __fileBeforePos = 0;
    __politician = None
    __landParser = None

    def __init__(self, file):
        print("Politician Property parse")
        self.__file = file
        self.__landParser = LandParser()

    def setPolitican(self,politican):
        self.__politician = politican

    def parse(self):
        self.__file.seek(self.__politician.getPoliticianFilePosition)
        self.checkPropertyPosition()
        # return self.__politician


    def checkPropertyPosition(self):

        # for i in range(0, self.__fileSize):
        statement = True
        while statement:
            self.__fileBeforePos = self.__file.tell()
            string = self.__file.readline()
            self.__filePos = self.__file.tell()
            if self.__file.tell() < self.__politician.getPoliticianFileEndPosition:
                # print("pos : ", self.__file.tell() , " O K")
                self.checkDivide(string)
            else:
                statement = False



    def checkDivide(self, string):
        tokenList = string.split()
        if len(tokenList) > 1 :
            self.checkPropertyDivide(tokenList)


    def checkPropertyDivide(self, tokenList):
        if tokenList[0] == "▶" :
            if tokenList[1] == "토지(소계)" :
                self.addLandProperty(tokenList)

            elif tokenList[1] == "건물(소계)" :
                getProperty = self.__politician.getPoliticianLandProperty
                if getProperty != None :
                    getProperty.setFileEndPosition =  self.__fileBeforePos

                self.addRealEstate(tokenList)

            elif tokenList[1] == "부동산에" :
                getProperty = self.__politician.getPoliticianRealEstate
                if getProperty != None :
                    getProperty.setFileEndPosition =  self.__fileBeforePos

                self.addRealRight(tokenList)
            elif tokenList[1] == "예금(소계)" :
                getProperty = self.__politician.getPoliticianRealRight
                if getProperty != None :
                    getProperty.setFileEndPosition =  self.__fileBeforePos

                self.addDeposit(tokenList)
            elif tokenList[1] == "정치자금법에" :
                getProperty = self.__politician.getPoliticianDeposit
                if getProperty != None :
                    getProperty.setFileEndPosition =  self.__fileBeforePos

                self.addPoliticDeposit(tokenList)
            elif tokenList[1] == "채무(소계)" :
                getProperty = self.__politician.getPoliticianPoliticDeposit
                if getProperty != None :
                    getProperty.setFileEndPosition =  self.__fileBeforePos

                self.addDebt(tokenList)

    '''
    텍스트 예시
    
    ▶ 토지(소계) 195,579 134,965 0 330,544 
    
    token 수가 6보다 많으면 형태 깨져있음.
    
    '''

    def addLandProperty(self,tokenList):

        if len(tokenList) <= 6 :
            pos = 2
            land = LandProperty()

            land.setpreValue = tokenList[pos]
            land.setTotalIncrease = tokenList[pos+1]
            land.setTotalDecrease = tokenList[pos+2]
            land.setPresentValue = tokenList[pos+3]

            land.setFileStartPosition = self.__fileBeforePos
            self.__politician.setPoliticianLandProperty = land
        else :
            # LandProperty.error()
            land = LandProperty()
            land.setFileStartPosition = self.__fileBeforePos
            self.__politician.setPoliticianLandProperty = land
            print(self.__politician.getPoliticianName + " Land Error")


    def addRealEstate(self, tokenList):

        if len(tokenList) <= 6 :
            pos = 2
            realEstate = RealEstate()

            realEstate.setpreValue = tokenList[pos]
            realEstate.setTotalIncrease = tokenList[pos+1]
            realEstate.setTotalDecrease = tokenList[pos+2]
            realEstate.setPresentValue = tokenList[pos+3]

            realEstate.setFileStartPosition = self.__fileBeforePos
            self.__politician.setPoliticianRealEstate = realEstate
        else :
            realEstate = RealEstate( )
            realEstate.setFileStartPosition = self.__fileBeforePos
            self.__politician.setPoliticianRealEstate = realEstate
            print(self.__politician.getPoliticianName + " realestate Error")

    def addRealRight(self, tokenList):

        if len(tokenList) <= 13 :
            pos = 9
            realRight = RealRight()

            realRight.setpreValue = tokenList[pos]
            realRight.setTotalIncrease = tokenList[pos+1]
            realRight.setTotalDecrease = tokenList[pos+2]
            realRight.setPresentValue = tokenList[pos+3]

            realRight.setFileStartPosition = self.__fileBeforePos
            self.__politician.setPoliticianRealRight = realRight
        else :
            realRight = RealRight()
            realRight.setFileStartPosition = self.__fileBeforePos
            self.__politician.setPoliticianRealRight = realRight
            print(self.__politician.getPoliticianName + " realright Error")

    def addDeposit(self, tokenList):

        if len(tokenList) <= 6 :
            pos = 2
            deposit = Deposit()

            deposit.setpreValue = tokenList[pos]
            deposit.setTotalIncrease = tokenList[pos+1]
            deposit.setTotalDecrease = tokenList[pos+2]
            deposit.setPresentValue = tokenList[pos+3]

            deposit.setFileStartPosition = self.__fileBeforePos
            self.__politician.setPoliticianDeposit = deposit
        else :
            deposit = Deposit()

            deposit.setFileStartPosition = self.__fileBeforePos
            self.__politician.setPoliticianDeposit = deposit
            print(self.__politician.getPoliticianName + " deposit Error")

    def addPoliticDeposit(self, tokenList):

        if len(tokenList) <= 14 :
            pos = 10
            politicDeposit = PoliticDeposit()

            politicDeposit.setpreValue = tokenList[pos]
            politicDeposit.setTotalIncrease = tokenList[pos+1]
            politicDeposit.setTotalDecrease = tokenList[pos+2]
            politicDeposit.setPresentValue = tokenList[pos+3]

            politicDeposit.setFileStartPosition = self.__fileBeforePos
            self.__politician.setPoliticianPoliticDeposit = politicDeposit
        else :
            politicDeposit = PoliticDeposit()

            politicDeposit.setFileStartPosition = self.__fileBeforePos
            self.__politician.setPoliticianPoliticDeposit = politicDeposit
            print(self.__politician.getPoliticianName + " politicDeposit Error")

    def addDebt(self, tokenList):

        if len(tokenList) <= 6 :
            pos = 2
            debt = Debt()

            debt.setpreValue = tokenList[pos]
            debt.setTotalIncrease = tokenList[pos+1]
            debt.setTotalDecrease = tokenList[pos+2]
            debt.setPresentValue = tokenList[pos+3]
            debt.setFileStartPosition = self.__fileBeforePos

            self.__politician.setPoliticianDebt = debt

        else :
            debt = Debt()

            debt.setFileStartPosition = self.__fileBeforePos
            self.__politician.setPoliticianDebt = debt
            print(self.__politician.getPoliticianName + " debt Error")
