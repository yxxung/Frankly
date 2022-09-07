'''

@Author 최제현

1차 작성
@date 22/08/19

열린국회정보 국회의원 인적사항 주소
https://open.assembly.go.kr/portal/infs/cont/infsContPage.do?cateId=NA11000


openAPI 주소
https://open.assembly.go.kr/portal/openapi/nwvrqwxyaytdsfvhu


'''


import json
import os
import traceback

from InformationClass.Party import Party


class Politician:


    def __init__(self, index=None):
        self._politicianID = index
        self._secretaru = None
        self._personalAssistant = None
        self._aide = None
        self._homePage = None
        self._email = None

    # PK 정치인ID
    @property
    def politicianID(self):
        return self._politicianID
    @politicianID.setter
    def politicianID(self,politicianID):
        self._politicianID = politicianID


    # 정치인 이름
    @property
    def politicianName(self):
        return self._politicianName
    @politicianName.setter
    def politicianName(self,politicianName):
        self._politicianName = politicianName

    # 정치인 한자이름
    @property
    def hanName(self):
        return self._hanName
    @hanName.setter
    def hanName(self,hanName):
        self._hanName = hanName

    #정치인 영어이름
    @property
    def engName(self):
        return self._engName
    @engName.setter
    def engName(self, engName):
        self._engName = engName

    # 음력생일
    @property
    def lunar(self):
        return self._lunar
    @lunar.setter
    def lunar(self, lunar):
        self._lunar = lunar

    # 생일

    @property
    def birthday(self):
        return self._birthday
    @birthday.setter
    def birthday(self, birthday):
        self._birthday =birthday

    # 당 ID
    @property
    def partyID(self):
        return self._partyID
    @partyID.setter
    def partyID(self,partyID):
        self._partyID = partyID

    # 당 이름
    @property
    def partyName(self):
        return self._partyName
    @partyName.setter
    def partyName(self, partyName):
        self._partyName = partyName

    # 지역ID

    @property
    def regionID(self):
        return self._regionID
    @regionID.setter
    def regionID(self, region):
        self._regionID = region

    @property
    def regionName(self):
        return self._regionName
    @regionName.setter
    def regionName(self, region):
        self._regionName = region

    # 선출횟수
    @property
    def selectNumber(self):
        return self._selectNumber

    @selectNumber.setter
    def selectNumber(self, selectNumber):
        if(selectNumber == "재선"):
            self._selectNumber = 2
        elif (selectNumber == "초선"):
            self._selectNumber = 1
        else:
            self._selectNumber = int(selectNumber.replace("선", ""))

    # 선출정보

    @property
    def selectInfo(self):
        return self._selectInfo

    @selectInfo.setter
    def selectInfo(self,selectInfo):
        self._selectInfo =selectInfo

    # 성별

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self,sex):
        self._sex = sex

    # contact

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, contact):
        self._contact = contact

    # email
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email

    # 홈페이지 주소

    @property
    def homePage(self):
        return self._homePage
    @homePage.setter
    def homePage(self, homePage):
        self._homePage = homePage

    # 보좌관

    @property
    def aide(self):
        return self._aide
    @aide.setter
    def aide(self, aide):
        self._aide = aide

    # 비서관

    @property
    def secretary(self):

        return self._secretary
    @secretary.setter
    def secretary(self, Secretary):
        self._secretary = Secretary

    # 비서

    @property
    def personalAssistant(self):
        return self._personalAssistant
    @personalAssistant.setter
    def personalAssistant(self, personalAssistant):
        self._personalAssistant = personalAssistant

    # -------------------------------------------------------------------

    def insert(self, cursor):
        sql = "INSERT INTO Politician VALUES('" + str(self.politicianID) +"','" + self.politicianName+"','" +\
              self.hanName+"','" + self.engName+"','" + self.lunar+"','" + self.birthday +"','" + str(self.partyID) +\
              "','" + self.partyName +"','" + str(self.regionID) +"','" + str(self.selectNumber) +\
              "','" + self.selectInfo +"','" + self.sex +"','" + self.contact +"','" + self.email +"','" + self.homePage +\
               "','" + self.aide + "','" + self.secretary +"','" + self.personalAssistant + "')"
        cursor.execute(sql)

    def selectNameID(self, cursor, input, column):

        try:
            if(column == "politicianID"):
                sql = "SELECT politicianName FROM Politician " +\
                      "WHERE politicianID = %s"
                cursor.execute(sql,(input[0]))
            elif(column == "politicianName"):
                sql = "SELECT politicianID, regionID FROM Politician " + \
                      "WHERE (politicianName = %s OR hanName = %s) AND partyName = %s"
                cursor.execute(sql,(input[0],input[0], input[1]))
            elif(column == "142"):
                sql = "SELECT politicianID, regionID FROM Politician " + \
                      "WHERE politicianName = %s AND regionID = 142"
                cursor.execute(sql,(input))

            return cursor.fetchall()
        except Exception as e:
            traceback.print_exc()
            return None


        cursor.execute(sql)


    # def selectPoliticiandef(self, cursor, value, column):
    #
    #     if(column == "politicianID"):
    #         sql = "SELECT * FROM Politician" + \
    #               "WHERE PoliticianID =" + value
    #     elif(column == "politicianName"):
    #         sql = "SELECT * FROM Politician" + \
    #               "WHERE PoliticianName =" + value





