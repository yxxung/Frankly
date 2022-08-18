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
        self.filePath = filePath
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
        self.file.close()


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
            if len(tokenList)<6:
                print(str(tokenList)+" politician format error \n" )
                tokenList.insert(4, "국회의원")
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
        newFile = open(self.filePath.replace(".txt",".json"), 'w', encoding='utf-8')
        newFile.write("[\n")
        for politician in self.politicianList :
            newFile.write("{")

            newFile.write("\n\"국회의원 이름\": ")
            newFile.write("\""+politician.getName.replace("\n","") + "\",\n")
            newFile.write("\"시작\": ")
            newFile.write(str(politician.getFilePosition) + ",\n")
            newFile.write("\"재산변동 total\": [{\n")

            count = 0
            for propertyChange in politician.politicianPropertyChangeList:
                count += 1
                if propertyChange != None:
                    newFile.write("\""+propertyChange.category +"\" :")
                    self.changeRecord(newFile, propertyChange)
                    if(count < len(politician.politicianPropertyChangeList)):
                        newFile.write("\t},\n")
                    else:
                        newFile.write("\t}\n")
            newFile.write("}],\n")
            newFile.write("\"재산변동\": [{\n")
            count = 0
            for propertyChange in politician.politicianPropertyChangeDetailList:
                count += 1
                if propertyChange != None:
                    section = propertyChange.category
                    newFile.write("\""+section +"\" :")
                    if section == "예금(소계)" or section ==  "정치자금(소계)" or propertyChange.deepCategory =="금융채무" or propertyChange.deepCategory == "상장주식" or propertyChange.deepCategory == "비상장주식":
                        self.changeDetailBankRecord(newFile, propertyChange)
                    else:
                        self.changeDetailRecord(newFile, propertyChange)
                    if(count < len(politician.politicianPropertyChangeDetailList)):
                        newFile.write("},\n")
                    else:
                        newFile.write("}\n")

            newFile.write("}],\n")
            newFile.write("\"국회의원끝\": ")
            newFile.write(str(politician.fileEndPosition) + "}\n,\n")
        newFile.close()

        # 마지막 콤마 삭제..
        newFile = open(self.filePath.replace(".txt",".json"), 'r+', encoding='utf-8')
        lines = newFile.readlines()
        newFile.seek(0)

        newFile.truncate()
        newFile.writelines(lines[:-1])

        newFile.write("]")
        newFile.close()



    def changeRecord(self, newFile, getProperty):
            # newFile.write("{\n\t\"시작\": ")
            # newFile.write(str(getProperty.fileStartPosition).replace(",","")+ ",\n")
            newFile.write("{\n\t\"종전가액\": ")
            newFile.write("\""+getProperty.previousValue.replace(",","")+"\""+ ",\n")
            newFile.write("\t\"증가액\": ")
            newFile.write("\""+getProperty.totalIncrease.replace(",","")+"\""+ ",\n")
            newFile.write("\t\"감소액\": ")
            newFile.write("\""+getProperty.totalDecrease.replace(",","")+"\""+ ",\n")
            newFile.write("\t\"현재가액\": ")
            newFile.write("\""+getProperty.presentValue.replace(",","")+"\""+ "\n")
            # newFile.write("\t\"재산끝\": ")
            # newFile.write(str(getProperty.fileEndPosition))

    def changeDetailRecord(self, newFile, getProperty):
        newFile.write("{\n\t\"종류\": ")
        newFile.write("\""+getProperty.category.replace(",","").split("(")[0]+"\"" + ",\n")
        newFile.write("\t\"상세종류\": ")
        newFile.write("\""+getProperty.deepCategory.replace(",","")+"\""+ ",\n")
        newFile.write("\t\"재산명세\": ")
        newFile.write("\""+getProperty.propertyDetail.replace(",","")+"\""+ ",\n")
        newFile.write("\t\"종전가액\": ")
        newFile.write("\""+getProperty.previousValue.replace(",","").split("(")[0]+"\""+ ",\n")
        newFile.write("\t\"증가액\": ")
        newFile.write("\""+getProperty.totalIncrease.replace(",","").split("(")[0]+"\""+ ",\n")
        newFile.write("\t\"감소액\": ")
        newFile.write("\""+getProperty.totalDecrease.replace(",","").split("(")[0]+"\""+ ",\n")
        newFile.write("\t\"현재가액\": ")
        newFile.write("\""+getProperty.presentValue.replace(",","").split("(")[0]+"\""+ ",\n")
        newFile.write("\t\"변동사유\": ")
        newFile.write("\""+getProperty.reason.replace(",","")+"\"")



    def changeDetailBankRecord(self, newFile, getProperty):
        newFile.write("{\n\t\"종류\": ")
        newFile.write("\""+getProperty.category.replace(",","").split("(")[0]+"\"" + ",\n")
        # newFile.write("\t\"상세종류\": ")
        # newFile.write("\""+getProperty.deepCategory.replace(",","")+"\""+ ",\n")
        if(len(getProperty.propertyDetail)!= 0):
            newFile.write("\t\"재산명세\": [\n")
        else:
            newFile.write("\t\"재산명세\": \"None\",\n")
        count = 0
        for propertyChange in getProperty.propertyDetail:
            count+=1
            newFile.write("\t\t{\n\t\t\"사명\": ")
            newFile.write("\"" + propertyChange.propertyDetail + "\"" + ",\n")
            newFile.write("\t\t\"종전가액\": ")
            newFile.write("\"" + str(propertyChange.previousValue) + "\"" + ",\n")
            newFile.write("\t\t\"증가액\": ")
            newFile.write("\"" + str(propertyChange.totalIncrease) + "\"" + ",\n")
            newFile.write("\t\t\"감소액\": ")
            newFile.write("\"" + str(propertyChange.totalDecrease) + "\"" + ",\n")
            newFile.write("\t\t\"현재가액\": ")
            newFile.write("\"" + str(propertyChange.presentValue) + "\"" + "\n")
            if(count < len(getProperty.propertyDetail)):
                newFile.write("\t\t},\n")
            else:
                newFile.write("\t\t}],\n")

        newFile.write("\t\"종전가액\": ")
        newFile.write("\""+getProperty.previousValue.replace(",","").split("(")[0]+"\""+ ",\n")
        newFile.write("\t\"증가액\": ")
        newFile.write("\""+getProperty.totalIncrease.replace(",","").split("(")[0]+"\""+ ",\n")
        newFile.write("\t\"감소액\": ")
        newFile.write("\""+getProperty.totalDecrease.replace(",","").split("(")[0]+"\""+ ",\n")
        newFile.write("\t\"현재가액\": ")
        newFile.write("\""+getProperty.presentValue.replace(",","").split("(")[0]+"\""+ ",\n")
        newFile.write("\t\"변동사유\": ")
        newFile.write("\""+getProperty.reason.replace(",","")+"\"")