'''
@Author 최제현
@Date 21/1/8

'''
from PropertyClasses.Parsers.Property import PoliticianPropertyParser
from PropertyClasses.PoliticianClass import Politician
import pickle


class PropertyMainParser:
    filePath = None
    file = None
    filePos = 0
    fileBeforePos = 0;
    fileSize = 0
    # __politicianPosition = None
    politicianList = None
    politicianParser = None



    def __init__(self, filePath):
        self.file = open(filePath, 'r', encoding ='utf-8')
        self.file.seek(0, 2)
        self.fileSize = self.file.tell()
        self.file.seek(0)
        # self.__politicianPosition = {}
        self.politicianList = []
        self.politicianParser = PoliticianPropertyParser(self.file)



    def parse(self):
        cnt = 0
        self.checkPoliticianPosition()

        # for index in range(len(self.politicianList)-1) :
        #     politician = self.politicianList[index]
        #     self.politicianParser.setPolitican(politician)
        #     self.politicianList[index] = self.politicianParser.parse()
        #     cnt += 1
        #     print(politician.getPoliticianName, " OK ", cnt)

        for politician in self.politicianList :
            self.politicianParser.setPolitican(politician)
            self.politicianParser.parse()
            print(politician.getPoliticianName, " OK ", cnt)
            cnt += 1


        print("test")
        self.recordPolitician()


    def checkPoliticianPosition(self):
        # for i in range(0, self.__fileSize):
        statement = True
        while statement:
            self.fileBeforePos = self.file.tell()
            string = self.file.readline()
            self.filePos = self.file.tell()
            if string != '' :
                # print("pos : ", self.__file.tell() , " O K")
                self.checkDivide(string)
            else:
                self.politicianList[len(self.politicianList)-1].\
                    setPoliticianFileEndPosition = self.fileBeforePos
                self.file.seek(0)
                statement = False



    def checkDivide(self, string):
        tokenList = string.split("|")
        if len(tokenList) > 3 :
            politicianListLen = len(self.politicianList)
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
        politician.setPoliticianFileEndPosition = self.fileBeforePos


    def recordPolitician(self):
        newFile = open('./politician.txt', 'w', encoding='utf-8')
        for politician in self.politicianList :
            newFile.write("\n-------------------")

            newFile.write("\n국회의원 이름: ")
            newFile.write(politician.getPoliticianName)

            newFile.write("\n시작: ")
            newFile.write(str(politician.getPoliticianFilePosition))


            getProperty = politician.getPoliticianLandProperty
            if getProperty != None:
                newFile.write("\n\n국회의원 토지: ")
                self.records(newFile, getProperty)


            getProperty = politician.getPoliticianRealEstate
            if getProperty != None:
                newFile.write("\n\n국회의원 건물: ")
                self.records(newFile, getProperty)

            getProperty = politician.getPoliticianRealRight
            if getProperty != None:
                newFile.write("\n\n국회의원 부동산: ")
                self.records(newFile, getProperty)


            getProperty = politician.getPoliticianDeposit
            if getProperty != None:
                newFile.write("\n\n국회의원 예금: ")
                self.records(newFile, getProperty)

            getProperty = politician.getPoliticianPoliticDeposit
            if getProperty != None:
                newFile.write("\n\n국회의원 정치예금: ")
                self.records(newFile, getProperty)


            getProperty = politician.getPoliticianDebt
            if getProperty != None:
                newFile.write("\n\n국회의원 빚: ")
                self.records(newFile, getProperty)

        newFile.write("\n국회의원끝: ")
        newFile.write(str(politician.getPoliticianFileEndPosition))

    def records(self, newFile, getProperty):
            newFile.write("\n시작: ")
            newFile.write(str(getProperty.getFileStartPosition))
            newFile.write("\n종전가액: ")
            newFile.write(getProperty.getPreviousValue)
            newFile.write("\n증가액: ")
            newFile.write(getProperty.getTotalIncrease)
            newFile.write("\n감소액: ")
            newFile.write(getProperty.getTotalDecresase)
            newFile.write("\n현재가액: ")
            newFile.write(getProperty.getPresentValue)
            newFile.write("\n재산끝: ")
            newFile.write(str(getProperty.getFileEndPoisition))
