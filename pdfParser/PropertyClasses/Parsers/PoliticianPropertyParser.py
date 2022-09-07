'''
@author 최제현

변경된 설계 반영 시작
@date 22/01/08

1차 리펙토링 시작
@date 22/08/01

1차 merge
@date 22/08/18

총 변환 액수 추가
@date 22/08/19

개선필요사항 :

우선 실거래가 무시하여 작성(22/08/19)
설계에 맞게 리펙토링 필요.


1차적으로 pdf 에서 추출한 txt문서로 변환한 테이블들을 양식에 맞게 처리하는 모듈

정치인들의 재산정보  JSON으로 변환


'''

from PropertyClasses.PropertyChangeClass import PropertyChange
import copy
import re


class PoliticianPropertyParser():

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
    # getter setter
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



#----------------------------------------------------------------------------

    # 전체적인 통제를 하는 메서드
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

            # end position 버그 처리
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
            print(str(tokenList) + "num position error \n")
            return

        pc = PropertyChange()
        pc.whos = tokenList[0]
        pc.category = section

        # 은행 및 증권리스트 저장용.


        tempReason = ""


        # 예외처리 6자리가 넘지 않는 경우, 세부 카테고리가 없는것임.
        if(len(tokenList) > 6):
            pc.deepCategory = tokenList[1]
        else:
            pc.deepCategory = section

        if(section == "증권(소계)"):
            pc.deepCategory = tokenList[1]
        elif(section == "예금(소계)"):
            pc.deepCategory = "예금"
        elif( section ==  "정치자금(소계)"):
            pc.deepCategory = "정치자금"
        #     은행 여러개 입력되어 있는 부분 처리.
        if section == "예금(소계)" or section ==  "정치자금(소계)" or pc.deepCategory == "금융채무" or pc.deepCategory == "상장주식" or pc.deepCategory == "비상장주식":
            pc.tempChangeDetail = tokenList[pos-1]
            detailTokenList = re.split(r', ',tokenList[pos-1].replace("(주)", "").replace("(보험)",""))
            tokenIndex = 0
            newList =[]
            if not(self.find0Numeric(tokenList)):
                return

            # 예외처리 은행 수가 너무 많아 나오는 파싱 오류 수정 디테일에 한버에 다 안붙여 나오는 오류 수정.
            if(detailTokenList[len(detailTokenList)-1].endswith(",")):
                string = self.file.readline().replace("\n","")
                token = string.split("|")
                if(len(token) == 2):
                    tempReason = token[1]
                tokenList[pos-1] = tokenList[pos-1] +token[0]
                detailTokenList = re.split(r', ',tokenList[pos-1].replace("(주)", "").replace("(보험)",""))


            for token in detailTokenList:
                # 예외처리  증감 없는 재산들 데이터 다루기 편하도록 변환

                # 파싱 오류로 마지막에 콤마 딸려옴


                if(not(token.endswith(")"))):
                    detailTokenList[tokenIndex] = detailTokenList[tokenIndex] + "(0 증가)"
                tokenIndex+=1


            # 만약 (0증가)처리까지 해주엇는데 토큰 크기가 너무 짧으면, 파싱하다가 오류가 났을 가능성이 큼 얘도 디테일에 한번에 다 안들어오는 오류
            # 예외처리.
            if self.find0Numeric(tokenList) and len(re.split(r' |\(',detailTokenList[len(detailTokenList)-1]))<=3:
                print("아마개행오류")
                print(tokenList)
                string = self.file.readline().replace("\n","")
                token = string.split("|")
                if(len(token) == 2):
                    print(token[1])
                tokenList[pos-1] = tokenList[pos-1] +token[0]
                detailTokenList = re.split(r', ',tokenList[pos-1].replace("(주)", "").replace("(보험)",""))

            # 각 은행별 증감사항 변경
            for token in detailTokenList:
                tempReason = ""
                tempTokenList = re.split(r' |\(', token)





                # # ETF이름들 ;;
                # if (tempTokenList[0] == "KODEX"):
                #     tempTokenList[0] += " " + tempTokenList[1]
                #     tempTokenList.pop(1)
                # elif (tempTokenList[0] == "Standard"):
                #     tempTokenList[0] += " " + tempTokenList[1] + " " + tempTokenList[2]
                #     tempTokenList.pop(1)
                #     tempTokenList.pop(1)


                blankCount = 0
                for token2 in tempTokenList:
                    # 파싱 잘못된것 삭제
                    if(token2 == ""):
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
                            tempTokenList[0] += tempTokenList[index+1]
                        for count in range(numPos-1):
                            tempTokenList.pop(1)

                # 증가 감소 위치 찾기
                pos2 = len(tempTokenList)-1
                if(pos2 <=1):
                    break
                for indexCount in range(len(tempTokenList)):
                    if(tempTokenList[indexCount] == "증가)" or tempTokenList[indexCount] == "감소)" or tempTokenList[indexCount] == "가)"  or tempTokenList[indexCount] == "소)"):
                        pos2 = indexCount
                        break

                # 예외처리 띄어쓰기 오입력
                pos3 = pos2-2
                if(tempTokenList[pos3] == "주"):
                    tempTokenList[pos3-1] += tempTokenList[pos3]
                    tempTokenList.pop(pos3)
                    pos2-=1

                elif(tempTokenList[pos3+1] == "주"):
                    pos3+=1
                    tempTokenList[pos3-1] += tempTokenList[pos3]
                    tempTokenList.pop(pos3)
                    pos2-=1

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
                        # if(detailChange.presentValue.isnumeric() and detailChange.totalIncrease.isnumeric()):
                        if(self.isNumeric(detailChange.presentValue) and self.isNumeric(detailChange.totalIncrease)):
                            detailChange.previousValue = float(detailChange.presentValue) - float(detailChange.totalIncrease)
                        else:
                            print(str(tempTokenList) + "not digit\n")
                            continue
                    elif(tempTokenList[pos2] == "감소)" or tempTokenList[pos2] == "소)"):
                        if(tempTokenList[pos2] == "소)"):
                            pos2 -= 1
                        detailChange.totalIncrease = "0"
                        detailChange.totalDecrease = tempTokenList[pos2-1].replace(",","")
                        # if(detailChange.presentValue.isnumeric()and detailChange.totalIncrease.isnumeric()):
                        if(self.isNumeric(detailChange.presentValue) and self.isNumeric(detailChange.totalIncrease)):
                            detailChange.previousValue = float(detailChange.presentValue) + float(detailChange.totalDecrease)
                        else:
                            print(str(tempTokenList) + "not digit\n")
                            continue

                    else:
                        print(str(tempTokenList) + "증감 인식불가 예외처리")
                    newList.append(detailChange)
                else:
                    if(tempTokenList[pos2] == "증가)" or tempTokenList[pos2] == "가)"):
                        if(tempTokenList[pos2] == "가)"):
                            pos2 -= 1
                        detailChange.totalIncrease = tempTokenList[pos2-1].replace(",","")
                        detailChange.totalDecrease = "0주"
                        # if(detailChange.presentValue.replace("주","").isnumeric() and detailChange.totalIncrease.replace("주","").isnumeric()):
                        if(self.isNumeric(detailChange.presentValue.replace("주","")) and self.isNumeric(detailChange.totalIncrease.replace("주",""))):
                            detailChange.previousValue = str(float(detailChange.presentValue.replace("주","")) - float(detailChange.totalIncrease.replace("주",""))) + "주"
                        else:
                            print(str(tempTokenList) + "not digit\n")
                    elif(tempTokenList[pos2] == "감소)" or tempTokenList[pos2] == "소)"):
                        if(tempTokenList[pos2] == "소)"):
                            pos2 -= 1
                        detailChange.totalIncrease = "0주"
                        detailChange.totalDecrease = tempTokenList[pos2-1].replace(",","")
                        # if(detailChange.presentValue.replace("주","").isnumeric() and detailChange.totalIncrease.replace("주","").isnumeric()):
                        if(self.isNumeric(detailChange.presentValue.replace("주","")) and self.isNumeric(detailChange.totalIncrease.replace("주",""))):
                            detailChange.previousValue = str(float(detailChange.presentValue.replace("주","")) + float(detailChange.totalDecrease.replace("주",""))) + "주"
                        else:
                            print(str(tempTokenList) + "not digit\n")
                    else:
                        print(str(tempTokenList) + "not up/down 증감 인식불가\n")

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
            if(tempReason == ""):
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
                # 국회의원 마지막 위치에 왓으면 총계정리.
                tokenList = string.split("|")
                if tokenList[0].startswith("총") :
                    list = self.propertyChangeList
                    list[len(list)-1].fileEndPosition = self.fileBeforePos
                    self.addPropertyChange(tokenList, "총계")

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
            if(section == "총계"):
                pc.propertyDetail = tokenList[pos+4].replace("\n","")
                pc.fileEndPosition = self.politician.fileEndPosition
            self.propertyChangeList.append(pc)


    # legacy
    # 실거래가 예외처리
    def numericValidCheck(self, tokenList):
        count = 0
        pos = 0
        for index in range(len(tokenList)):
            # 숫자가 4번 연속으로 나오면 금액변동임
            if str(tokenList[index]).replace(",","").replace("주","").isdigit():
                # count += 1
                return pos
            elif str(tokenList[index].split("(")[0].replace(",","")).isdigit():
                # count += 1
                return pos
            elif tokenList[index] == '-':
                # count += 1
                return pos
            else:
                pos += 1

        # 숫자 4번 연속으로 오면 현재가 정보임. 파싱 정확도 상승으로 우선 주석처리
        # if count >= 4:
        #     return pos
        # else:
        #     print(self.politician.name + "numeric valid check Error")
        #     return -1

        # legacy
        # 실거래가 예외처리
    def find0Numeric(self, tokenList):
        count = 0

        for index in range(len(tokenList)):
            if(tokenList[index] == "0"):
                count +=1


        if(count == 4):
            return False
        else:
            return True

    def isNumeric(self,value):
        flag = True

        try:
            num = float(value)
            # NaN check
            flag = num == num

        except:
            flag = False

        return flag

