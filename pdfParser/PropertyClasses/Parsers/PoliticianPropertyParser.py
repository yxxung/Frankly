import re
from PropertyClasses.PropertyChangeClass import PropertyChange
import copy
import re


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
        detailList = self.propertyChangeDetailList
        detailList[len(detailList)-1].fileEndPosition = self.fileBeforePos

        self.politician.politicianPropertyChangeList = copy.deepcopy(self.propertyChangeList)
        self.propertyChangeList = []

        self.politician.politicianPropertyChangeDetailList = copy.deepcopy(self.propertyChangeDetailList)
        self.propertyChangeDetailList = []

        # return self.__politician


    # 앞서 만든 소계 리스트를 하나하나 끝내서, 첨부터 끝까지 세부 변경사항 parse
    def checkPropoertyDetail(self):


        for propertyChange in self.propertyChangeList:

            self.file.seek(propertyChange.fileStartPosition)
            # 첫라인 패스
            string = self.file.readline()


            # if(propertyChange.fileEndPosition == None):
            #     propertyChange.fileEndPosition = self.politician.fileEndPosition
            # end position 버그
            while(self.file.tell()<propertyChange.fileEndPosition):
                string = self.file.readline()
                tokenList = string.split("|")
                if(tokenList[0] == "본인" or tokenList[0] =="배우자"):
                    self.addPropertyDetailChange(tokenList, propertyChange.category)
    # def addDepositDetailChange(self, tokenList, section):
    #     print("stub")
    #     tokenList[len(tokenList)-1] = tokenList[len(tokenList)-1].replace("\n", "")
    #     pos = self.numericValidCheck(tokenList)
    #     if pos == -1:
    #         print(tokenList)
    #         return
    #
    #     pc = PropertyChange()
    #     pc.whos = tokenList[0]


    # 디테일
    def addPropertyDetailChange(self,tokenList, section):

        tokenList[len(tokenList)-1] = tokenList[len(tokenList)-1].replace("\n", "")
        pos = self.numericValidCheck(tokenList)
        if pos == -1:
            print(str(tokenList) + "num position error \n")
            return

        pc = PropertyChange()
        pc.whos = tokenList[0]

        # 6자리가 넘지 않는 경우, 세부 카테고리가 없는것임.
        if(len(tokenList) > 6):
            pc.deepCategory = tokenList[1]
        else:
            pc.deepCategory = "None"
        if section == "예금(소계)" or section ==  "정치자금(소계)" or pc.deepCategory == "금융채무" or pc.deepCategory == "상장주식" or pc.deepCategory == "비상장주식":
            detailTokenList = re.split(r', ',tokenList[pos-1].replace("(주)", "").replace("(보험)",""))
            tokenIndex = 0
            for token in detailTokenList:
                # 증감 없는 재산들 데이터 다루기 편하도록 변환
                if(not(token.endswith(")"))):
                    detailTokenList[tokenIndex] = detailTokenList[tokenIndex] + "(0 증가)"
                tokenIndex+=1

            newList =[]

            # 각 은행별 증감사항 변경
            for token in detailTokenList:
                tempTokenList = re.split(r' |\(', token)

                # ETF이름들 ;;
                if (tempTokenList[0] == "KODEX"):
                    tempTokenList[0] += " " + tempTokenList[1]
                    tempTokenList.pop(1)
                elif (tempTokenList[0] == "Standard"):
                    tempTokenList[0] += " " + tempTokenList[1] + " " + tempTokenList[2]
                    tempTokenList.pop(1)
                    tempTokenList.pop(1)


                blankCount = 0
                for token in tempTokenList:
                    # 파싱 잘못된것 삭제
                    if(token == ""):
                        blankCount +=1

                if(blankCount != 0):
                    for count in range(blankCount):
                        tempTokenList.remove("")


                detailChange = PropertyChange()

                if(len(tempTokenList)>4):
                    numPos = self.numericValidCheck(tempTokenList)
                    # 띄어쓰기 있는 사명들 처리.
                    if(numPos != 1 and (numPos != None)):
                        for index in range(numPos-1):
                            tempTokenList[0] += " " + tempTokenList[index+1]
                        for count in range(numPos-1):
                            tempTokenList.pop(1)

                if(len(tempTokenList)<=4):
                    pos2 = len(tempTokenList)-1
                else:
                    # 가끔 자리 오류 나는것.
                    pos2 = 3




                # 은행이름1
                detailChange.propertyDetail = tempTokenList[0].replace(")", "")
                # 현재가액
                detailChange.presentValue = tempTokenList[pos2-2].replace(",","")
                detailChange.category = tempTokenList[1]
                # 증감액
                if(pc.deepCategory != "상장주식" and pc.deepCategory != "비상장주식"):
                    if(tempTokenList[pos2] == "증가)" or tempTokenList[pos2] == "가)"):
                        if(tempTokenList[pos2] == "가)"):
                            pos2 -= 1
                        detailChange.totalIncrease = tempTokenList[pos2-1].replace(",","")
                        detailChange.totalDecrease = "0"
                        if(detailChange.presentValue.isnumeric() and detailChange.totalIncrease.isnumeric()):
                            detailChange.previousValue = float(detailChange.presentValue) - float(detailChange.totalIncrease)
                        else:
                            print(str(tempTokenList) + "not digit\n")
                            continue
                    elif(tempTokenList[pos2] == "감소)" or tokenList[pos2] == "소)"):
                        if(tempTokenList[pos2] == "소)"):
                            pos2 -= 1
                        detailChange.totalIncrease = "0"
                        detailChange.totalDecrease = tempTokenList[pos2-1].replace(",","")
                        if(detailChange.presentValue.isnumeric() and detailChange.totalIncrease.isnumeric()):
                            detailChange.previousValue = float(detailChange.presentValue) + float(detailChange.totalDecrease)
                        else:
                            print(str(tempTokenList) + "not digit\n")
                            continue

                    else:
                        print(str(tempTokenList) + "somethin went wrong")
                    newList.append(detailChange)
                else:
                    if(tempTokenList[pos2] == "증가)" or tempTokenList[pos2] == "가)"):
                        if(tempTokenList[pos2] == "가)"):
                            pos2 -= 1
                        detailChange.totalIncrease = tempTokenList[pos2-1].replace(",","")
                        detailChange.totalDecrease = "0주"
                        if(detailChange.presentValue.replace("주","").isnumeric() and detailChange.totalIncrease.replace("주","").isnumeric()):
                            detailChange.previousValue = str(float(detailChange.presentValue.replace("주","")) - float(detailChange.totalIncrease.replace("주",""))) + "주"
                        else:
                            print(str(tempTokenList) + "not digit\n")
                    elif(tempTokenList[pos2] == "감소)" or tokenList[pos2] == "소)"):
                        if(tempTokenList[pos2] == "소)"):
                            pos2 -= 1
                        detailChange.totalIncrease = "0주"
                        detailChange.totalDecrease = tempTokenList[pos2-1].replace(",","")
                        if(detailChange.presentValue.replace("주","").isnumeric() and detailChange.totalIncrease.replace("주","").isnumeric()):
                            detailChange.previousValue = str(float(detailChange.presentValue.replace("주","")) + float(detailChange.totalDecrease.replace("주",""))) + "주"
                        else:
                            print(str(tempTokenList) + "not digit\n")
                    else:
                        print(str(tempTokenList) + "not up/down\n")
                    newList.append(detailChange)

            pc.propertyDetail = newList
        else:
            # 은행 등 아닐경우 간단처리
            pc.propertyDetail = tokenList[pos-1]

        pc.previousValue = tokenList[pos].replace("\n","")
        pc.totalIncrease = tokenList[pos+1].replace("\n","")
        pc.totalDecrease = tokenList[pos+2].replace("\n","")
        pc.presentValue = tokenList[pos+3].replace("\n","")
        pc.category = section

        if(pos+5==len(tokenList)):
            pc.reason = tokenList[pos+4]
        else:
            pc.reason = "None"

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
            list = self.propertyChangeList



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

        elif tokenList[0] == "▶ 채권(소계)" :

            list = self.propertyChangeList
            if(len(list) == 0):
                self.addPropertyChange(tokenList, "채권(소계)")
            else:
                list[len(list)-1].fileEndPosition = self.fileBeforePos
                self.addPropertyChange(tokenList, "채권(소계)")

        elif tokenList[0] == "▶ 증권(소계)" :

            list = self.propertyChangeList
            if(len(list) == 0):
                self.addPropertyChange(tokenList, "증권(소계)")
            else:
                list[len(list)-1].fileEndPosition = self.fileBeforePos
                self.addPropertyChange(tokenList, "증권(소계)")

        elif tokenList[0] == "▶ 유가증권(소계)" :

            list = self.propertyChangeList
            if(len(list) == 0):
                self.addPropertyChange(tokenList, "증권(소계)")
            else:
                list[len(list)-1].fileEndPosition = self.fileBeforePos
                self.addPropertyChange(tokenList, "증권(소계)")

        elif tokenList[0] == "▶ 현금(소계)" :

            list = self.propertyChangeList
            if(len(list) == 0):
                self.addPropertyChange(tokenList, "현금(소계)")
            else:
                list[len(list)-1].fileEndPosition = self.fileBeforePos
                self.addPropertyChange(tokenList, "현금(소계)")

        elif tokenList[0] == "▶ 회원권(소계)" :

            list = self.propertyChangeList
            if(len(list) == 0):
                self.addPropertyChange(tokenList, "회원권(소계)")
            else:
                list[len(list)-1].fileEndPosition = self.fileBeforePos
                self.addPropertyChange(tokenList, "회원권(소계)")
        elif tokenList[0].startswith("▶ 합명") :
            list = self.propertyChangeList
            if(len(list) == 0):
                self.addPropertyChange(tokenList, "출자지분(소계)")
            else:
                list[len(list)-1].fileEndPosition = self.fileBeforePos
                self.addPropertyChange(tokenList, "출자지분(소계)")

        elif tokenList[0].startswith("▶") :
            list = self.propertyChangeList
            if(len(list) == 0):
                self.addPropertyChange(tokenList, "기타")
            else:
                list[len(list)-1].fileEndPosition = self.fileBeforePos
                self.addPropertyChange(tokenList, "기타")
        elif tokenList[0].startswith("총") :
            list = self.propertyChangeList
            list[len(list)-1].fileEndPosition = self.fileBeforePos


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
            if str(tokenList[index]).replace(",","").replace("주","").isnumeric():
                # count += 1
                return pos
            elif str(tokenList[index].split("(")[0].replace(",","")).isnumeric():
                # count += 1
                return pos
            elif tokenList[index] == '-':
                # count += 1
                return pos
            else:
                pos += 1

        # if count >= 4:
        #     return pos
        # else:
        #     print(self.politician.name + "numeric valid check Error")
        #     return -1


