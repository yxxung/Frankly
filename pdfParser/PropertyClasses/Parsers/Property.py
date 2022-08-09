import re
from PropertyClasses.DebtClass import Debt
from PropertyClasses.DepositClass import Deposit
from PropertyClasses.LandPropertyClass import LandProperty
from PropertyClasses.Parsers.Land import LandParser
from PropertyClasses.PoliticDepositClass import PoliticDeposit
from PropertyClasses.PropertyChangeClass import PropertyChange
from PropertyClasses.RealEstateClass import RealEstate
from PropertyClasses.RealRightClass import RealRight


class PoliticianPropertyParser():
    file = None
    filePos = 0
    fileBeforePos = 0;
    politician = None
    landParser = None

    def __init__(self, file):
        print("Politician Property parse")
        self.file = file
        self.landParser = LandParser()

    def setPolitican(self,politican):
        self.politician = politican

    def parse(self):
        self.file.seek(self.politician.getPoliticianFilePosition)
        self.checkPropertyPosition()
        # return self.__politician


    def checkPropertyPosition(self):

        # for i in range(0, self.__fileSize):
        statement = True
        while statement:
            self.fileBeforePos = self.file.tell()
            string = self.file.readline()
            self.filePos = self.file.tell()
            if self.file.tell() < self.politician.getPoliticianFileEndPosition:
                # print("pos : ", self.__file.tell() , " O K")
                self.checkDivide(string)
            else:
                statement = False



    def checkDivide(self, string):
        tokenList = string.split("|")
        if len(tokenList) > 1 :
            self.checkPropertyDivide(tokenList)


    def checkPropertyDivide(self, tokenList):
        if tokenList[0] == "▶ 토지(소계)" :
            # self.addLandProperty(tokenList)
            self.addPropertyChange(tokenList, "landtotal")
        elif tokenList[0] == "▶ 건물(소계)" :
            # getProperty = self.politician.getPoliticianLandProperty
            # if getProperty != None :
            #     getProperty.setFileEndPosition =  self.fileBeforePos
            #
            # self.addRealEstate(tokenList)
            self.addPropertyChange(tokenList, "buildingtotal")
        elif tokenList[0].startswith("▶ 부동산에") :
            # getProperty = self.politician.getPoliticianRealEstate
            # if getProperty != None :
            #     getProperty.setFileEndPosition =  self.fileBeforePos
            #
            # self.addRealRight(tokenList)
            self.addPropertyChange(tokenList, "realtotal")
        elif tokenList[0] == "▶ 예금(소계)" :
            # getProperty = self.politician.getPoliticianRealRight
            # if getProperty != None :
            #     getProperty.setFileEndPosition =  self.fileBeforePos

            # self.addDeposit(tokenList)
            self.addPropertyChange(tokenList, "deposittotal")
        elif tokenList[0].startswith("▶ 정치자금법에") :
            # getProperty = self.politician.getPoliticianDeposit
            # if getProperty != None :
            #     getProperty.setFileEndPosition =  self.fileBeforePos
            #
            # self.addPoliticDeposit(tokenList)
            self.addPropertyChange(tokenList, "politicDepoisittotal")
        elif tokenList[0] == "▶ 채무(소계)" :
            # getProperty = self.politician.getPoliticianPoliticDeposit
            # if getProperty != None :
            #     getProperty.setFileEndPosition =  self.fileBeforePos
            #
            # self.addDebt(tokenList)
            self.addPropertyChange(tokenList, "debttotal")


    def addLandProperty(self,tokenList):

        if len(tokenList) <= 6 :
            pos = 2
            land = LandProperty()

            land.setPreviousValue = tokenList[pos]
            land.setTotalIncrease = tokenList[pos+1]
            land.setTotalDecrease = tokenList[pos+2]
            land.setPresentValue = tokenList[pos+3]

            land.setFileStartPosition = self.fileBeforePos
            self.politician.setPoliticianLandProperty = land
        else :
            # LandProperty.error()
            land = LandProperty()

            if self.numericValidCheck(tokenList, land):
                land.setFileStartPosition = self.fileBeforePos
                self.politician.setPoliticianLandProperty = land
                print(self.politician.getPoliticianName + " land Error but inserted")
            else:
                print(self.politician.getPoliticianName + " land Error cant insert data")



    def addRealEstate(self, tokenList):

        if len(tokenList) <= 6 :
            pos = 2
            realEstate = RealEstate()

            realEstate.setPreviousValue = tokenList[pos]
            realEstate.setTotalIncrease = tokenList[pos+1]
            realEstate.setTotalDecrease = tokenList[pos+2]
            realEstate.setPresentValue = tokenList[pos+3]

            realEstate.setFileStartPosition = self.fileBeforePos
            self.politician.setPoliticianRealEstate = realEstate
        else :
            realEstate = RealEstate( )

            if self.numericValidCheck(tokenList, realEstate):
                realEstate.setFileStartPosition = self.fileBeforePos
                self.politician.setPoliticianRealEstate = realEstate
                print(self.politician.getPoliticianName + " realestate Error but inserted")
            else:
                print(self.politician.getPoliticianName + " realestate Error cant insert data")


    def addRealRight(self, tokenList):

        if len(tokenList) <= 13 :
            pos = 9
            realRight = RealRight()

            realRight.setPreviousValue = tokenList[pos]
            realRight.setTotalIncrease = tokenList[pos+1]
            realRight.setTotalDecrease = tokenList[pos+2]
            realRight.setPresentValue = tokenList[pos+3]

            realRight.setFileStartPosition = self.fileBeforePos
            self.politician.setPoliticianRealRight = realRight
        else :
            realRight = RealRight()

            if self.numericValidCheck(tokenList, realRight):
                realRight.setFileStartPosition = self.fileBeforePos
                self.politician.setPoliticianRealRight = realRight
                print(self.politician.getPoliticianName + " realright Error but inserted")
            else:
                print(self.politician.getPoliticianName + " realright Error cant insert data")



            print(self.politician.getPoliticianName + " realright Error")

    def addDeposit(self, tokenList):

        if len(tokenList) <= 6 :
            pos = 2
            deposit = Deposit()

            deposit.setPreviousValue = tokenList[pos]
            deposit.setTotalIncrease = tokenList[pos+1]
            deposit.setTotalDecrease = tokenList[pos+2]
            deposit.setPresentValue = tokenList[pos+3]

            deposit.setFileStartPosition = self.fileBeforePos
            self.politician.setPoliticianDeposit = deposit
        else :
            deposit = Deposit()

            # deposit.setFileStartPosition = self.__fileBeforePos
            # self.__politician.setPoliticianDeposit = deposit
            # print(self.__politician.getPoliticianName + " deposit Error")

            if self.numericValidCheck(tokenList, deposit):
                deposit.setFileStartPosition = self.fileBeforePos
                self.politician.setPoliticianDeposit = deposit
                print(self.politician.getPoliticianName + " deposit Error but inserted")
            else:
                print(self.politician.getPoliticianName + " deposit Error cant insert data")


    def addPoliticDeposit(self, tokenList):

        if len(tokenList) <= 14 :
            pos = 10
            politicDeposit = PoliticDeposit()

            politicDeposit.setPreviousValue = tokenList[pos]
            politicDeposit.setTotalIncrease = tokenList[pos+1]
            politicDeposit.setTotalDecrease = tokenList[pos+2]
            politicDeposit.setPresentValue = tokenList[pos+3]

            politicDeposit.setFileStartPosition = self.fileBeforePos
            self.politician.setPoliticianPoliticDeposit = politicDeposit
        else :
            politicDeposit = PoliticDeposit()

            if self.numericValidCheck(tokenList, politicDeposit):
                politicDeposit.setFileStartPosition = self.fileBeforePos
                self.politician.setPoliticianDeposit = politicDeposit
                print(self.politician.getPoliticianName + " politic deposit Error but inserted")
            else:
                print(self.politician.getPoliticianName + " politic deposit Error cant insert data")

    def addDebt(self, tokenList):

        if len(tokenList) <= 6 :
            pos = 2
            debt = Debt()

            debt.setPreviousValue = tokenList[pos]
            debt.setTotalIncrease = tokenList[pos+1]
            debt.setTotalDecrease = tokenList[pos+2]
            debt.setPresentValue = tokenList[pos+3]
            debt.setFileStartPosition = self.fileBeforePos

            self.politician.setPoliticianDebt = debt

        else :
            debt = Debt()

            if self.numericValidCheck(tokenList, debt):
                debt.setFileStartPosition = self.fileBeforePos
                self.politician.setPoliticianDeposit = debt
                print(self.politician.getPoliticianName + " debt Error but inserted")
            else:
                print(self.politician.getPoliticianName + " debt Error cant insert data")

    def numericValidCheck(self, tokenList, prop):
        count = 0
        pos = 0
        for index in range(len(tokenList)-1):
            # 숫자가 4번 연속으로 나오면 금액변동임
            if str(tokenList[index]).replace(",","").isdigit():
                count += 1
                if count == 1 :
                    pos = index
            if count == 4:
                break
            elif count > 4:
                print(self.politician.getPoliticianName + "numeric valid check Error")
                return False


        prop.setPreviousValue = tokenList[pos]
        prop.setTotalIncrease = tokenList[pos+1]
        prop.setTotalDecrease = tokenList[pos+2]
        if str(tokenList[pos+3]).isnumeric():
            prop.setPresentValue = tokenList[pos+3]
            return True
        else:
            regex = re.compile("\d+")
            result = regex.findall(tokenList[pos+3])
            temp = ""
            if result != None :
                for num in result:
                    temp = temp + num
                temp = format(int(temp), ',')
                prop.setPresentValue = temp
                return True
            else :
                return False

    def addPropertyChange(self, tokenList, section):

        if len(tokenList) <= 6 :
            pos = 1
            pc = PropertyChange()

            pc.setPreviousValue = tokenList[pos].replace("\n","")
            pc.setTotalIncrease = tokenList[pos+1].replace("\n","")
            pc.setTotalDecrease = tokenList[pos+2].replace("\n","")
            pc.setPresentValue = tokenList[pos+3].replace("\n","")
            pc.setFileStartPosition = self.fileBeforePos
            pc.setCategory = section

            self.politician.setPoliticianPropertyChangeList(pc)

        else :
            debt = Debt()

            if self.numericValidCheck(tokenList, debt):
                debt.setFileStartPosition = self.fileBeforePos
                self.politician.setPoliticianDeposit = debt
                print(self.politician.getPoliticianName + " debt Error but inserted")
            else:
                print(self.politician.getPoliticianName + " debt Error cant insert data")