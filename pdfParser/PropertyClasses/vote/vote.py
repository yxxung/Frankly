"""
국회의원 표결정보

https://open.assembly.go.kr/portal/data/service/selectServicePage.do/OPR1MQ000998LC12535
https://wonhwa.tistory.com/entry/Python-%EA%B3%B5%EA%B3%B5%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%8F%AC%ED%84%B8%EC%9D%98-OPEN-API-%EC%82%AC%EC%9A%A9-%EB%B0%A9%EB%B2%952
"""
import datetime
import time
import traceback

import pymysql
import requests

from InformationClass.Politician import Politician
from InformationClass.openAPI import openAPI
from ConferenceBillLaw import ConferenceBillLaw

import csv
import json

class Vote:

    def __init__(self):
        self._politicianID = None
        self._voteURL = None
        self._voteResult = None
        self._billNumber = None

    @property
    def politicianID(self):
        return self._politicianID

    @politicianID.setter
    def politicianID(self, politicianID):
        self._politicianID = politicianID

    @property
    def billNumber(self):
        return self._billNumber

    @billNumber.setter
    def billNumber(self, billNumber):
        self._billNumber = billNumber

    @property
    def voteDate(self):
        return self._voteDate

    @voteDate.setter
    def voteDate(self, voteDate):
        self._voteDate = datetime.datetime.strptime(voteDate, '%Y%m%d %H%M%S')

    @property
    def voteResult(self):
        return self._voteResult

    @voteResult.setter
    def voteResult(self, voteResult):
        self._voteResult = voteResult

    @property
    def voteURL(self):
        return self._voteURL

    @voteURL.setter
    def voteURL(self, voteURL):
        self._voteURL = voteURL

    # ----------------------------------------------
    #
    # def csvToJson(self):
    #     csvfile = open('vote21.csv', 'r',encoding="UTF-8")
    #     jsonfile = open('vote21.json', 'w',encoding="UTF-8")
    #     # 리턴해주는 의원 ID랑 동일 확인 << 아마 동일하지싶음.
    #     fieldnames = ("AGE","BILL_NO","billTitle","VOTE_DATE","HG_NM","HJ_NM","POLY_NM","RESULT_VOTE_MOD","BILL_URL","BILL_NAME_URL")
    #     reader = csv.DictReader(csvfile, fieldnames)
    #     for row in reader:
    #         json.dump(row, jsonfile)
    #         jsonfile.write('\n')
    #     csvfile.close()
    #     jsonfile.close()
    #
    # def jsonPrepro(self):
    #     jsonfile = open('vote21.json', 'r',encoding="UTF-8")
    #     parsedJson = json.load(jsonfile)
    #

    def parseVote(self):
        con, cur = self.dbConnect()
        pp = Politician()
        politicianList = pp.selectALL(cur)
        cb = ConferenceBillLaw()
        billLawList = cb.selectAll(cur)
        for billLaw in billLawList:
            billLaw.checked = False

        for billLaw in billLawList:
            billLaw.checked = True
            if(billLaw.billNumber == 2110278):
                break
        voteAPI = openAPI()
        voteAPI.setAPIInfo(cur, "vote")
        billLawAPI = openAPI()
        billLawAPI.setAPIInfo(cur, "ConferenceBillLaw")

        # json 데이터 이상.. 2002년 데이터도 들어가있음 걸러내야함.
        # for billLaw in billLawList:
        #     billLawParams = {'Key': billLawAPI.secretKey, 'Type': 'json', \
        #                       'pIndex': 1, 'pSize' : 100, 'AGE':'21', \
        #                       'BILL_NO' : billLaw.billNumber}
        #     response = requests.get(billLawAPI.URL, params=billLawParams)
        #     contents = json.loads(response.text)["nwbpacrgavhjryiph"][1]["row"]
        #     billLaw.billLawAPIID = contents[0]["BILL_ID"]
        #     billLaw.update(cur, billLaw.billLawAPIID, billLaw.billNumber)
        #     con.commit()
        #     time.sleep(0.05)
        # print("billLaw id parse finish")

        for billLaw in billLawList:
            if billLaw.checked == True:
                print("이미 완료된 bill law ")
                continue
            voteParams = {'Key': voteAPI.secretKey, 'Type': 'json', \
                      'pIndex': 1, 'pSize' : 1000, 'AGE':21, "BILL_ID" : billLaw.billLawAPIID}
            response = json.loads(requests.get(voteAPI.URL, params=voteParams).text)
            if response.get('nojepdqqaweusdfbi') == None:
                print("해당되는 데이터를 찾지 못습니다.")
                continue

            contents = response["nojepdqqaweusdfbi"][1]["row"]

            for voteJson in contents:
                # json 바로삽입입
                vote = Vote()
                for politician in politicianList:
                    if politician.politicianName == voteJson['HG_NM'] and \
                        politician.partyName == voteJson['POLY_NM'] and \
                        politician.regionName == voteJson['ORIG_NM']:
                        vote.politicianID = politician.politicianID
                if vote.politicianID == None:
                    print(voteJson['HG_NM'] + " 사퇴")
                    continue
                vote.billNumber = voteJson['BILL_NO']
                vote.voteDate = voteJson['VOTE_DATE']
                vote.voteResult = voteJson['RESULT_VOTE_MOD']
                vote.voteURL = voteJson['BILL_URL']
                try:
                    vote.insert(cur)

                except Exception as e:
                    print("출석정보 중복. 더 이상 삽입이 필요없거나 데이터 확인이 필요합니다.")
                    break
            con.commit()
            print("billlaw vote information insert " + voteJson['BILL_NO'])
        print("vote parse end")

    def insert(self,cursor):

        try:
            sql = "INSERT INTO Vote VALUES(%s, %s, %s, %s ,%s ,%s)"
            cursor.execute(sql,(None,self.politicianID, self.billNumber, self.voteDate, self.voteResult, self.voteURL))
        except pymysql.err.IntegrityError as e:
            code, msg = e.args
            print("표결데이터 중복")
            sql = "SELECT count(voteID) from Vote"
            cursor.execute(sql)
            selectcount = cursor.fetchone()
            sql = "ALTER TABLE Vote AUTO_INCREMENT = %s"
            cursor.execute(sql,(selectcount[0]))
            print("auto increment set : " + str(selectcount[0]))
            raise Exception('vote 중복')
        except Exception as e:
            traceback.print_exc()




    def dbConnect(self):
        # dbinfoDir = "E:\work\Frankly\pdfParser\InformationClass/dbinfo.info"
        dbinfoDir = "D:\code\Frankly\pdfParser\InformationClass/dbinfo.info"
        with open(dbinfoDir, encoding="UTF8") as dbInfo:

            IP  = dbInfo.readline().split(" ")[1].replace("\n", "")
            port = dbInfo.readline().split(" ")[1].replace("\n", "")
            userID = dbInfo.readline().split(" ")[1].replace("\n", "")
            password = dbInfo.readline().split(" ")[1].replace("\n", "")
            dbname = dbInfo.readline().split(" ")[1].replace("\n", "")

            connection = pymysql.connect(host= IP, port=int(port), user=userID, passwd=password, db=dbname, charset="utf8")
            cursor = connection.cursor()

            dbInfo.close()
            return connection, cursor

vote = Vote()
vote.parseVote()