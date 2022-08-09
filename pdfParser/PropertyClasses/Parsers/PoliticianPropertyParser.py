import re
from PropertyClasses.DebtClass import Debt
from PropertyClasses.DepositClass import Deposit
from PropertyClasses.LandPropertyClass import LandProperty
from PropertyClasses.Parsers.Land import LandParser
from PropertyClasses.PoliticDepositClass import PoliticDeposit
from PropertyClasses.PropertyChangeClass import PropertyChange
from PropertyClasses.RealEstateClass import RealEstate
from PropertyClasses.RealRightClass import RealRight
import copy


class PoliticianPropertyParser():
    # file = None
    # filePos = 0
    # fileBeforePos = 0;
    # politician = None
    # landParser = None
    # propertyChangeList = []

    def __init__(self, file):
        print("Politician Property parse")
        self.file = None
        self.filePos = None
        self.fileBeforePos = None
        self.politician= None
        self.propertyChangeList = []
        self.file = file
        self.landParser = LandParser()

    @property
    def getLandParser(self):
        return self.landParser
    @getLandParser.setter
    def setLandParser(self, landParser):
        self.landParser = landParser

    @property
    def getFile(self):
        return self.file
    @getFile.setter
    def setFile(self, File):
        self.setFile = File

    @property
    def getFilePos(self):
        return self.filePos
    @getFilePos.setter
    def setFilePos(self,filePos):
        self.filePos = filePos

    @property
    def getFileBeforePos(self):
        return self.fileBeforePos

    @getFileBeforePos.setter
    def setFileBeforePos(self, fileBeforePos):
        self.fileBeforePos = fileBeforePos

    @property
    def getPolitican(self):
        return self.politician

    @getPolitican.setter
    def setPolitican(self,politican):
        self.politician = politican

    @property
    def getPropertyChangeList(self):
        return self.propertyChangeList

    @getPropertyChangeList.setter
    def setPropertyChangeList(self, propertyChangeList):
        self.propertyChangeList = propertyChangeList

    def parse(self):
        self.file.seek(self.politician.filePosition)
        self.checkPropertyPosition()
        list = self.propertyChangeList
        list[len(list)-1].fileEndPosition = self.fileBeforePos
        self.politician.politicianPropertyChangeList = copy.deepcopy(self.propertyChangeList)
        self.propertyChangeList = []
        # return self.__politician


    def checkPropertyPosition(self):

        # for i in range(0, self.__fileSize):
        statement = True
        while statement:
            self.fileBeforePos = self.file.tell()
            string = self.file.readline()
            self.filePos = self.file.tell()

            politicianEnd = self.politician.fileEndPosition
            if(politicianEnd == None):
                list = self.politician.politicianPropertyChangeList
                politicianEnd = list[len(list)-1].fileEndPosition
            if self.file.tell() < politicianEnd:
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
            self.addPropertyChange(tokenList, "토지(소계)")
        elif tokenList[0] == "▶ 건물(소계)" :
            # getProperty = self.politician.getPoliticianLandProperty
            # if getProperty != None :
            #     getProperty.setFileEndPosition =  self.fileBeforePos
            #
            # self.addRealEstate(tokenList)
            list = self.propertyChangeList
            if(len(list) == 0):
                self.addPropertyChange(tokenList, "건물(소계)")
            else:
                list[len(list)-1].fileEndPosition = self.fileBeforePos
                self.addPropertyChange(tokenList, "건물(소계)")
        elif tokenList[0].startswith("▶ 부동산에") :
            # getProperty = self.politician.getPoliticianRealEstate
            # if getProperty != None :
            #     getProperty.setFileEndPosition =  self.fileBeforePos
            #
            # self.addRealRight(tokenList)
            list = self.propertyChangeList
            if(len(list) == 0):
                self.addPropertyChange(tokenList, "부동산(소계)")
            else:
                list[len(list)-1].fileEndPosition = self.fileBeforePos
                self.addPropertyChange(tokenList, "부동산(소계)")
        elif tokenList[0] == "▶ 예금(소계)" :
            # getProperty = self.politician.getPoliticianRealRight
            # if getProperty != None :
            #     getProperty.setFileEndPosition =  self.fileBeforePos

            # self.addDeposit(tokenList)
            list = self.propertyChangeList
            if(len(list) == 0):
                self.addPropertyChange(tokenList, "예금(소계)")
            else:
                list[len(list)-1].fileEndPosition = self.fileBeforePos
                self.addPropertyChange(tokenList, "예금(소계)")

        elif tokenList[0].startswith("▶ 정치자금법에") :
            # getProperty = self.politician.getPoliticianDeposit
            # if getProperty != None :
            #     getProperty.setFileEndPosition =  self.fileBeforePos
            #
            # self.addPoliticDeposit(tokenList)
            list = self.propertyChangeList
            if(len(list) == 0):
                self.addPropertyChange(tokenList, "정치자금(소계)")
            else:
                list[len(list)-1].fileEndPosition = self.fileBeforePos
                self.addPropertyChange(tokenList, "정치자금(소계)")

        elif tokenList[0] == "▶ 채무(소계)" :
            # getProperty = self.politician.getPoliticianPoliticDeposit
            # if getProperty != None :
            #     getProperty.setFileEndPosition =  self.fileBeforePos
            #
            # self.addDebt(tokenList)
            list = self.propertyChangeList
            if(len(list) == 0):
                self.addPropertyChange(tokenList, "채무(소계)")
            else:
                list[len(list)-1].fileEndPosition = self.fileBeforePos
                self.addPropertyChange(tokenList, "채무(소계)")



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

            self.propertyChangeList.append(pc)


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

