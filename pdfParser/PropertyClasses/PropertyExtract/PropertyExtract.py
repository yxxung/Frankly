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
        fileList = os.listdir(jsonDir)
        con, cur = self.dbConnect()

        for fileName in fileList:
            if(fileName.endswith(".json")):
                with open(jsonDir+"/"+fileName, encoding="UTF8") as jsonObject:
                    parsedJson = json.load(jsonObject)
                    print("stub")
                    for politician in parsedJson:

                        p = Politician(index=None)
                        politicianID = p.selectNameID(cursor= cur, value= politician["국회의원 이름"], column="politicianName")

                        property = Property()
                        propertyChange = PropertyChange()
                        propertyList = PropertyList()

                        # propertyList.propert



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


if option == '1':
    pe = PropertyExtract()
    pe.jsonParse()