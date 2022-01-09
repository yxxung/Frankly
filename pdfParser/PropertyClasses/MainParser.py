'''
@Author 최제현
@Date 21/1/8

'''
from PropertyClasses.PoliticianClass import Politician


class MainParser:
    __filePath = None
    __file = None
    __filePos = 0
    __fileBeforePos = 0;
    __fileSize = 0
    # __politicianPosition = None
    __politicianList = None



    def __init__(self, filePath):
        self.__file = open(filePath, 'r', encoding = 'utf-8')
        self.__file.seek(0, 2)
        self.__fileSize = self.__file.tell()
        self.__file.seek(0)
        # self.__politicianPosition = {}
        self.__politicianList = []



    def parse(self):
        self.checkPoliticianPosition()
        print("test")


    def checkPoliticianPosition(self):
        # for i in range(0, self.__fileSize):
        statement = True
        while statement:
            self.__fileBeforePos = self.__file.tell()
            string = self.__file.readline()
            if string != None :
                # print("pos : ", self.__file.tell() , " O K")
                self.checkDivide(string)
            else:
                self.__file.seek(0)
                break



    def checkDivide(self, string):
        tokenList = string.split()
        politicianListLen = len(self.__politicianList)
        if len(tokenList) > 3 :
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
                filePosition= self.__file.tell()
            )
            self.__politicianList.append(politician)

    def addPoliticianFileEndPosition(self, len):
        politician = self.__politicianList[len-1]
        politician.setPoliticianFileEndPosition = self.__fileBeforePos
