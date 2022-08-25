from Property import Property
from PropertyChange import PropertyChange
from PropertyList import PropertyList
from InformationClass.Politician import Politician

import json
import sys
import os
import pymysql


class PropertyExtract:


    def jsonParse(self):

        jsonDir = 'E:\work\Frankly\pdfParser\PropertyClasses\Parsers\moneyTXT'
        # jsonDir = 'D:\code\Frankly\pdfParser\PropertyClasses\moneyTXT'
        fileList = os.listdir(jsonDir)

        sectionBank = ["예금", "정치자금"]
        categoryBank = ["상장주식", "비상장주식", "금융채무"]
        p = Politician(index=None)


        for fileName in fileList:
            if(fileName.endswith(".json")):
                with open(jsonDir+"/"+fileName, encoding="UTF8") as jsonObject:
                    parsedJson = json.load(jsonObject)
                    self.parsePropertyList(parsedJson)
                    self.parseProperty(parsedJson)
            print("stub")





                    # for change in politician["재산변동"]:
                    #     property = Property()
                    #     property.politicianID = politicianID
                    #     property.propertyDetail = change["재산명세"]
                    #     property.presentPrice = change["현재가액"]
    def parseProperty(self, parsedJson):

        con, cur = self.dbConnect()


        for politician in parsedJson:
            p = Politician()
            result = p.selectNameID(cursor= cur, value= politician["국회의원 이름"], column="politicianName")
            if(result != None):
                politicianID = result[0]
            else:
                print(politician["국회의원 이름"] + "사퇴")
                continue
        con.commit()
        con.close()


    def parsePropertyList(self, parsedJson):


        con, cur = self.dbConnect()

        jsonDir = 'E:\work\Frankly\pdfParser\PropertyClasses\Parsers\moneyTXT'
        # jsonDir = 'D:\code\Frankly\pdfParser\PropertyClasses\moneyTXT'
        propertyListCategory = []

        print("stub")

        for politician in parsedJson:

            for change in politician["재산변동"]:
                change["상세종류"] = change["상세종류"].replace(" ", "")
                propertyList = PropertyList()
                if not(change in propertyListCategory):
                    propertyList.section = change["종류"]
                    propertyList.kind = change["상세종류"]
                    propertyList.relation = change["관계"]
                    propertyListCategory.append(propertyList)
                else:
                    continue

        for propertyList in propertyListCategory:
            result = propertyList.selectOne(cur, section=propertyList.section, \
                                            kind= propertyList.kind, \
                                            relation=propertyList.relation)
            if result == None:
                propertyList.insert(cur)
                con.commit()
            else:
                continue

                # id 재정렬
        # sql = "SET @CNT =0"
        # cur.execute(sql)
        # sql = "UPDATE PropertyList SET propertyListID = @CNT:=@CNT+1 order by propertyListID,relation"
        # cur.execute(sql)
        con.commit()
        con.close()

    def dbConnect(self):
        dbinfoDir = "E:\work\Frankly\pdfParser\InformationClass/dbinfo.info"
        # dbinfoDir = "D:\code\Frankly\pdfParser\InformationClass/dbinfo.info"
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


if option == '1':
    pe = PropertyExtract()
    pe.jsonParse()