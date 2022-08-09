'''
@Author 최제현
@Date 21/1/8

'''
from PropertyClasses.Parsers.PoliticianPropertyParser import PoliticianPropertyParser
from PropertyClasses.PoliticianClass import Politician
import pickle


class PropertyMainParser:
    # filePath = None
    # file = None
    # filePos = 0
    # fileBeforePos = 0;
    # fileSize = 0
    # # __politicianPosition = None
    # politicianList = None
    # politicianParser = None



    def __init__(self, filePath):
        self.file = None
        self.filePos = None
        self.fileBeforePos = None
        self.fileSize = None
        self.politicianPosition = None
        self.politicianList = None
        self.politicianParser = None
        self.file = open(filePath, 'r', encoding ='utf-8')
        self.file.seek(0, 2)
        self.fileSize = self.file.tell()
        self.file.seek(0)
        # self.__politicianPosition = {}
        self.politicianList = []
        self.politicianParser = PoliticianPropertyParser(self.file)

    @property
    def getFilePath(self):
        return self.filePath
    @getFilePath.setter
    def setFilePath(self, filepath):
        self.filePath = filepath

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
    def getFileSize(self):
        return self.fileSize

    @getFileSize.setter
    def setFileSize(self, fileSize):
        self.fileSize = fileSize

    @property
    def getPoliticinPosition(self):
        return self.politicianPosition

    @getPoliticinPosition.setter
    def setPoliticinPosition(self, politicinPosition):
        self.politicianPosition = politicinPosition

    @property
    def getPoliticianList(self):
        return self.politicianList

    @getPoliticianList.setter
    def setPoliticianList(self, politicianList):
        self.politicianList = politicianList

    @property
    def getPoliticianParser(self):
        return self.politicianParser

    @getPoliticianParser.setter
    def setPoliticianParser(self, politicianParser):
        self.politicianParser = politicianParser


        # fileBeforePos = 0;
    # fileSize = 0
    # # __politicianPosition = None
    # politicianList = None
    # politicianParser = None

    def parse(self):
        cnt = 0
        self.checkPoliticianPosition()

        # for index in range(len(self.politicianList)-1) :
        #     politician = self.politicianList[index]
        #     self.politicianParser.setPolitican(politician)
        #     self.politicianList[index] = self.politicianParser.parse()
        #     cnt += 1
        #     print(politician.getPoliticianName, " OK ", cnt)

        for politician in self.getPoliticianList :
            parser = self.politicianParser
            parser.politician = politician
            parser.parse()
            print(politician.name, " OK ", cnt)
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
                    fileEndPosition = self.fileBeforePos
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
        politician.fileEndPosition = self.fileBeforePos


    def recordPolitician(self):
        newFile = open('./politician.txt', 'w', encoding='utf-8')
        for politician in self.politicianList :
            newFile.write("\n-------------------")

            newFile.write("\n국회의원 이름: ")
            newFile.write(politician.getName)

            newFile.write("\n시작: ")
            newFile.write(str(politician.getFilePosition))


            for propertyChange in politician.politicianPropertyChangeList:
                if propertyChange != None:
                    newFile.write("\n\n"+propertyChange.category +" :")
                    self.records(newFile, propertyChange)
            newFile.write("\n국회의원끝: ")
            newFile.write(str(politician.fileEndPosition))



    def records(self, newFile, getProperty):
            newFile.write("\n시작: ")
            newFile.write(str(getProperty.fileStartPosition))
            newFile.write("\n종전가액: ")
            newFile.write(getProperty.previousValue)
            newFile.write("\n증가액: ")
            newFile.write(getProperty.totalIncrease)
            newFile.write("\n감소액: ")
            newFile.write(getProperty.totalDecrease)
            newFile.write("\n현재가액: ")
            newFile.write(getProperty.presentValue)
            newFile.write("\n재산끝: ")
            newFile.write(str(getProperty.fileEndPosition))
