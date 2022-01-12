'''
@Author 최제현
@Date 21/1/8

'''
from PropertyClasses.Property import PoliticianPropertyParser
from PropertyClasses.PoliticianClass import Politician


class PropertyMainParser:
    filePath = None
    file = None
    __filePos = 0
    __fileBeforePos = 0;
    __fileSize = 0
    # __politicianPosition = None
    politicianList = None
    politicianParser = None



    def __init__(self, filePath):
        self.file = open(filePath, 'r', encoding = 'utf-8')
        self.file.seek(0, 2)
        self.__fileSize = self.file.tell()
        self.file.seek(0)
        # self.__politicianPosition = {}
        self.politicianList = []
        self.politicianParser = PoliticianPropertyParser()



    def parse(self):
        self.checkPoliticianPosition()

        # for Politician in self.politicianList :
        #     self.politicianParser.setPolitican(Politician)
        #     self.politicianParser.parse()

        print("test")


    def checkPoliticianPosition(self):
        # for i in range(0, self.__fileSize):
        statement = True
        while statement:
            self.__fileBeforePos = self.file.tell()
            string = self.file.readline()
            if string != '' :
                # print("pos : ", self.__file.tell() , " O K")
                self.checkDivide(string)
            else:
                print("siiok")
                self.file.seek(0)
                break



    def checkDivide(self, string):
        tokenList = string.split()
        politicianListLen = len(self.politicianList)
        if len(tokenList) > 3 :
            self.checkPoliticianDivide(tokenList, politicianListLen)


    def checkPoliticianDivide(self, tokenList, politicianListLen):

        if tokenList[1] == "국회" :
            # 국회의원 정보 시작
            # 각 국회의원들 블록 지정
            if politicianListLen > 0 :
                self.addPoliticianFileEndPosition(politicianListLen)
            self.addPolitician(tokenList, 1)
            # print(tokenList[5], " add OK")

        else :

            if tokenList[2] == "국회" :
                if politicianListLen > 0 :
                    self.addPoliticianFileEndPosition(politicianListLen)
                self.addPolitician(tokenList, 2)
                # print(tokenList[6], " add OK")



    def addPolitician(self, tokenList, startPos):

            # 딕셔너리 버전
            # self.__politicianPosition[tokenList[startPost + 4]] = self.__file.tell()
            politician = Politician(
                name = tokenList[startPos + 4],
                belong = tokenList[startPos],
                position = tokenList[startPos + 2],
                filePosition= self.file.tell()
            )
            self.politicianList.append(politician)

    def addPoliticianFileEndPosition(self, len):
        politician = self.politicianList[len-1]
        politician.setPoliticianFileEndPosition = self.__fileBeforePos
