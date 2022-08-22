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

        # jsonDir = 'E:\work\Frankly\pdfParser\PropertyClasses\Parsers\moneyTXT'
        jsonDir = 'D:\code\Frankly\pdfParser\PropertyClasses\moneyTXT'
        fileList = os.listdir(jsonDir)
        con, cur = self.dbConnect()
        sectionBank = ["예금", "정치자금"]
        categoryBank = ["상장주식", "비상장주식", "금융채무"]
        p = Politician(index=None)

        for fileName in fileList:
            if(fileName.endswith(".json")):
                with open(jsonDir+"/"+fileName, encoding="UTF8") as jsonObject:
                    parsedJson = json.load(jsonObject)
                    print("stub")

                    for politician in parsedJson:


                        result = p.selectNameID(cursor= cur, value= politician["국회의원 이름"], column="politicianName")
                        if(result != None):
                            politicianID = result[0]
                        else:
                            print(politician["국회의원 이름"] + "사퇴")
                            continue


                        propertyChange = PropertyChange()


                        for change in politician["재산변동"]:
                            propertyList = PropertyList()
                            result = propertyList.selectOne(cur, section=change["종류"], \
                                                            kind= change["상세종류"].replace(" ",""), \
                                                            relation=change["관계"])

                            if result == None:
                                # if not(change["종류"] in sectionBank or change["상세종류"] in categoryBank):
                                propertyList.section = change["종류"]
                                propertyList.kind = change["상세종류"]
                                propertyList.relation = change["관계"]
                                propertyList.insert(cur)
                            else:
                                continue

                    con.commit()
                    con.close()

                    print("stub")
                    # for change in politician["재산변동"]:
                    #     property = Property()
                    #     property.politicianID = politicianID
                    #     property.propertyDetail = change["재산명세"]
                    #     property.presentPrice = change["현재가액"]



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


option = sys.argv[1]


if option == '1':
    pe = PropertyExtract()
    pe.jsonParse()