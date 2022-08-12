import re
from PropertyClasses.PropertyChangeClass import PropertyChange
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
        self.propertyChangeDetailList = []
        self.file = file

    # property
#----------------
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

    @property
    def getPropertyChangeDetailList(self):
        return self.propertyChangeDetailList

    @getPropertyChangeList.setter
    def setPropertyChangeDetailList(self, propertyChangeList):
        self.propertyChangeDetailList = propertyChangeList


#----------------------


    def parse(self):
        self.file.seek(self.politician.filePosition)
        self.checkPropertyPosition()
        list = self.propertyChangeList
        list[len(list)-1].fileEndPosition = self.fileBeforePos
        self.checkPropoertyDetail()
        self.politician.politicianPropertyChangeList = copy.deepcopy(self.propertyChangeList)
        self.propertyChangeList = []
        self.politician.politicianPropertyChangeDetailList = copy.deepcopy(self.propertyChangeDetailList)
        self.propertyChangeDetailList = []
        # return self.__politician


    def checkPropoertyDetail(self):

        for propertyChange in self.propertyChangeList:
            self.file.seek(propertyChange.fileStartPosition)
            self.fileBeforePos = self.file.tell()
            # 첫라인 패스
            string = self.file.readline()
            self.filePos = self.file.tell()

            while(self.file.tell()<propertyChange.fileEndPosition):
                string = self.file.readline()
                tokenList = string.split("|")
                if(tokenList[0] == "본인" or tokenList[0] =="배우자"):
                    self.addPropertyDetailChange(tokenList, propertyChange.category)


    # 디테일
    def addPropertyDetailChange(self,tokenList, section):

        tokenList[len(tokenList)-1] = tokenList[len(tokenList)-1].replace("\n", "")
        pos = self.numericValidCheck(tokenList)
        if pos == -1:
            print(tokenList)
            return

        pc = PropertyChange()
        pc.whos = tokenList[0]
        if(len(tokenList) > 6):
            pc.deepCategory = tokenList[1]
        else:
            pc.deepCategory = "empty"
        pc.propertyDetail = tokenList[pos-1]
        pc.previousValue = tokenList[pos].replace("\n","")
        pc.totalIncrease = tokenList[pos+1].replace("\n","")
        pc.totalDecrease = tokenList[pos+2].replace("\n","")
        pc.presentValue = tokenList[pos+3].replace("\n","")
        pc.category = section

        if(pos+5==len(tokenList)):
            pc.reason = tokenList[pos+4]
        else:
            pc.reason = "empty"

        self.propertyChangeDetailList.append(pc)



    # total 변화, 섹션별 위치 저장
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


    # 섹션별 위치 저장 실행
    def checkDivide(self, string):
        tokenList = string.split("|")
        if len(tokenList) > 1 :
            self.checkPropertyDivide(tokenList)



    # 파싱후 판단
    # 카테고리 지정
    def checkPropertyDivide(self, tokenList):
        if tokenList[0] == "▶ 토지(소계)" :
            # self.addLandProperty(tokenList)
            self.addPropertyChange(tokenList, "토지(소계)")
        elif tokenList[0] == "▶ 건물(소계)" :
            list = self.propertyChangeList
            if(len(list) == 0):
                self.addPropertyChange(tokenList, "건물(소계)")
            else:
                list[len(list)-1].fileEndPosition = self.fileBeforePos
                self.addPropertyChange(tokenList, "건물(소계)")
        elif tokenList[0].startswith("▶ 부동산에") :
            list = self.propertyChangeList
            if(len(list) == 0):
                self.addPropertyChange(tokenList, "부동산(소계)")
            else:
                list[len(list)-1].fileEndPosition = self.fileBeforePos
                self.addPropertyChange(tokenList, "부동산(소계)")
        elif tokenList[0] == "▶ 예금(소계)" :
            list = self.propertyChangeList
            if(len(list) == 0):
                self.addPropertyChange(tokenList, "예금(소계)")
            else:
                list[len(list)-1].fileEndPosition = self.fileBeforePos
                self.addPropertyChange(tokenList, "예금(소계)")

        elif tokenList[0].startswith("▶ 정치자금법에") :
            list = self.propertyChangeList
            if(len(list) == 0):
                self.addPropertyChange(tokenList, "정치자금(소계)")
            else:
                list[len(list)-1].fileEndPosition = self.fileBeforePos
                self.addPropertyChange(tokenList, "정치자금(소계)")

        elif tokenList[0] == "▶ 채무(소계)" :

            list = self.propertyChangeList
            if(len(list) == 0):
                self.addPropertyChange(tokenList, "채무(소계)")
            else:
                list[len(list)-1].fileEndPosition = self.fileBeforePos
                self.addPropertyChange(tokenList, "채무(소계)")

        elif tokenList[0] == "▶ 회원권(소계)" :

            list = self.propertyChangeList
            if(len(list) == 0):
                self.addPropertyChange(tokenList, "회원권(소계)")
            else:
                list[len(list)-1].fileEndPosition = self.fileBeforePos
                self.addPropertyChange(tokenList, "회원권(소계)")

    # 카테고리 지정된것을 기준으로 위치 저장 등
    def addPropertyChange(self, tokenList, section):

        if len(tokenList) <= 6 :
            pos = 1
            pc = PropertyChange()

            pc.previousValue = tokenList[pos].replace("\n","")
            pc.totalIncrease = tokenList[pos+1].replace("\n","")
            pc.totalDecrease = tokenList[pos+2].replace("\n","")
            pc.presentValue = tokenList[pos+3].replace("\n","")
            pc.fileStartPosition = self.fileBeforePos
            pc.category = section
            self.propertyChangeList.append(pc)


    # legacy
    # 실거래가 예외처리
    def numericValidCheck(self, tokenList):
        count = 0
        pos = 0
        for index in range(len(tokenList)):
            # 숫자가 4번 연속으로 나오면 금액변동임
            if str(tokenList[index]).replace(",","").isdigit():
                count += 1
            elif str(tokenList[index].split("(")[0].replace(",","")).isdigit():
                count += 1
            elif tokenList[index] == '-':
                count += 1
            else:
                pos += 1

        if count >= 4:
            return pos
        else:
            print(self.politician.name + "numeric valid check Error")
            return -1


