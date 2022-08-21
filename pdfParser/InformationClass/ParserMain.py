import pymysql
# 파일이름, class명
from Politician import Politician
from Region import Region
from Party import Party
from datetime import datetime
import traceback


import sys
import json
import os

class ParserMain:
    politicianList = []
    regionList = []
    partyList = []


    def parseJsonToPolitician(self):

        self.jsonParse()

        self.makeRegion()

        self.makeParty()

        self.setPoliticianPartyRegionID()

        try:
            self.partyInsert()
        except Exception as e:
            traceback.print_exc()
            print("party insert error")
        try:
            self.regionInsert()
        except Exception as e:
            traceback.print_exc()
            print("region insert error")

        try:
            self.politicianInsert()
        except Exception as e:
            traceback.print_exc()
            print("politician insert error")

        print("stub")


    def jsonParse(self):

        jsonDir = 'E:\work\Frankly\pdfParser\InformationClass\Json'
        fileList = os.listdir(jsonDir)

        for fileName in fileList:
            with open(jsonDir+"/"+fileName, encoding="UTF8") as jsonObject:
                parsedJson = json.load(jsonObject)
                print("stub")
                for index in range(len(parsedJson)-1):
                    # log 삽입

                    jsonIndex = index+1
                    politician = Politician(jsonIndex)
                    politician.politicianName = parsedJson[jsonIndex]['HG_NM']
                    politician.hanName = parsedJson[jsonIndex]['HJ_NM']
                    politician.engName = parsedJson[jsonIndex]['ENG_NM']
                    politician.lunar = parsedJson[jsonIndex]['BTH_GBN_NM']
                    politician.birthday =  parsedJson[jsonIndex]['BTH_DATE']
                    politician.partyName =  parsedJson[jsonIndex]['POLY_NM']
                    politician.regionName =  parsedJson[jsonIndex]['ORIG_NM']
                    politician.selectNumber =  parsedJson[jsonIndex]['REELE_GBN_NM']
                    politician.selectInfo =  parsedJson[jsonIndex]['UNITS']
                    politician.sex =  parsedJson[jsonIndex]['SEX_GBN_NM']
                    politician.contact =  parsedJson[jsonIndex]['TEL_NO']
                    politician.email =  parsedJson[jsonIndex]['E_MAIL']
                    politician.homePage =  parsedJson[jsonIndex]['HOMEPAGE']
                    politician.aide =  parsedJson[jsonIndex]['STAFF']
                    politician.secretary =  parsedJson[jsonIndex]['SECRETARY']
                    politician.personalAssistant =  parsedJson[jsonIndex]['SECRETARY2']
                    self.politicianList.append(politician)
            # print("stub")

        jsonObject.close()


    def makeRegion(self):
        regionID = 0
        for politiican in self.politicianList:
            if not(politiican.regionName in self.regionList):
                region = Region(
                    regionName = politiican.regionName
                )
                self.regionList.append(region)

        #   정렬 기준: 지역이름
        self.regionList.sort(key=lambda region:region.regionName)

        for region in self.regionList:
            regionID+=1
            region.regionID = regionID


    def makeParty(self):
        partyID = 0
        for politiican in self.politicianList:
            if not(politiican.partyName in self.partyList):
                party = Party(
                    partyName = politiican.partyName
                )
                party.count = 1
                self.partyList.append(party)
            else:
                partyIndex = self.partyList.index(politiican.partyName)
                self.partyList[partyIndex].count += 1

        #   정렬 기준: 당원 수
        self.partyList.sort(key=lambda party:party.count,reverse=True)

        for party in self.partyList:
            partyID+=1
            party.partyID = partyID


        # print("stub")

    def setPoliticianPartyRegionID(self):

        for politician in self.politicianList:
            regionIndex = self.regionList.index(politician.regionName)
            politician.regionID = self.regionList[regionIndex].regionID
            partyIndex = self.partyList.index(politician.partyName)
            politician.partyID = self.partyList[partyIndex].partyID

    def partyInsert(self):
        connnection, cursor = self.dbConnect()
        for party in self.partyList:
            party.insert(cursor)

        connnection.commit()
        connnection.close()

    def regionInsert(self):
        connnection, cursor = self.dbConnect()
        for region in self.regionList:
            region.insert(cursor)

        connnection.commit()
        connnection.close()

    def politicianInsert(self):

        connnection, cursor = self.dbConnect()
        for politician in self.politicianList:
            politician.insert(cursor)

        connnection.commit()
        connnection.close()


    def dbConnect(self):
        dbinfoDir = "E:\work\Frankly\pdfParser\InformationClass/dbinfo.info"
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


option = sys.argv[1]
parser = ParserMain()


if option == '1':

    parser.parseJsonToPolitician()



