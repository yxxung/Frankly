'''
@Author 최제현
@Date 22/8/

국회공보 주소

https://www.assembly.go.kr/portal/bbs/B0000059/list.do?pageIndex=1&menuNo=600103&searchWrdMb=&searchDtGbnMb=c0&pageUnit=10&searchDtGbn=c0&sdate=&edate=&cl1Cd=&searchCnd=1&searchWrd=%EC%9E%AC%EC%82%B0

json에 저장된 정치인 재산 변동 데이터를 DB에 저장.

'''
from PropertyClasses.PropertyExtract.Property import Property
from PropertyClasses.PropertyExtract.PropertyChange import PropertyChange
from PropertyClasses.PropertyExtract.PropertyList import PropertyList
from InformationClass.Politician import Politician

import json
import sys
import os
import pymysql

# id 들 db에서 가져온뒤 캐시 하는걸로 고려 8/27
# 김병욱, 이수진 처리 동명이인
# property change reason 100에서 더 늘려야할듯
class PropertyExtract:




    def jsonParse(self):

        # jsonDir = 'E:\work\Frankly\pdfParser\PropertyClasses\Parsers\moneyTXT'
        jsonDir = 'D:\code\Frankly\pdfParser\PropertyClasses\moneyTXT'
        fileList = os.listdir(jsonDir)
        p = Politician(index=None)


        for fileName in fileList:
            if(fileName.endswith(".json")):
                with open(jsonDir+"/"+fileName, encoding="UTF8") as jsonObject:
                    parsedJson = json.load(jsonObject)
                    print("list parse")
                    self.parsePropertyList(parsedJson)
                    print("property parse")
                    self.parseProperty(parsedJson)
                    print("propertychange parse")
                    self.parsePropertyChange(parsedJson)
            # print("stub")

    def parseProperty(self, parsedJson):
        sectionList = [
            "예금",
            "정치자금",
            "금융채무",
            "상장주식",
            "비상장주식"
        ]
        con, cur = self.dbConnect()
        pl = PropertyList()
        pp = Property()
        p = Politician()
        for politician in parsedJson:
            result = p.selectNameID(cursor= cur, value= politician["국회의원 이름"], column="politicianName")
            if(result != None):
                politicianID = result[0]
            else:
                print(politician["국회의원 이름"] + "사퇴")
                continue

            for change in politician["재산변동"]:
                property = Property()
                section = change["종류"]
                kind = change["상세종류"].replace(" ", "")
                relation = change["관계"]
                result = pl.selectOne(cursor= cur,\
                                                     section=section,\
                                                     kind= kind,\
                                                     relation=relation)
                if(result != None):
                    property.propertyListID = result[0]
                else:
                    print(politician["국회의원 이름"] + section + kind + relation +"삽입오류")

                property.politicianID = politicianID

                if(change["상세종류"] in sectionList):
                    for detail in change["재산명세"]:
                        property.propertyDetail = detail["사명"]
                        property.presentPrice = detail["현재가액"]
                        property.insert(cur)
                        # commit 위치 차이 고려해보기.
                        con.commit()

                else:
                    property.propertyDetail = change["재산명세"]
                    property.presentPrice = change["현재가액"]
                    property.insert(cur)
                    con.commit()
        con.close()

    def parsePropertyChange(self, parsedJson):
        sectionList = [
            "예금",
            "정치자금",
            "금융채무",
            "상장주식",
            "비상장주식"
        ]
        con, cur = self.dbConnect()
        pl = PropertyList()
        pp = Property()
        p = Politician()
        for politician in parsedJson:


            result = p.selectNameID(cursor= cur, value= politician["국회의원 이름"], column="politicianName")
            if(result != None):
                politicianID = result[0]
            else:
                print(politician["국회의원 이름"] + "사퇴")
                continue


            for change in politician["재산변동"]:
                propertyChange = PropertyChange()

                propertyChange.politicianID = politicianID

                section = change["종류"]
                kind = change["상세종류"].replace(" ", "")
                relation = change["관계"]
                result = pl.selectOne(cursor= cur, \
                                      section=section, \
                                      kind= kind, \
                                      relation=relation)
                if(result != None):
                    propertyListID = result[0]
                else:
                    print(politician["국회의원 이름"] + section + kind + relation +" property List 검색오류")
                    continue


                if(change["상세종류"] in sectionList):
                    for detail in change["재산명세"]:
                        result = pp.selectOne(cursor= cur, \
                                              detail= detail["사명"], \
                                              politicianID = politicianID, \
                                              propertyListID = propertyListID, \
                                              price = detail["현재가액"]
                                              )
                        if(result != None):
                            propertyID = result[0]
                        else:
                            print(politician["국회의원 이름"] + section + kind + relation +"Property ID 검색오류")
                            # 없으면 삽입시도 하는게 코드 효율 높을 수도 있지만, 어차피 1년에 한번에 실행인데 굳이
                            continue
                        propertyChange.propertyID = propertyID
                        # 그냥 감소액 등 넣는거 고려
                        propertyChange.price = detail["현재가액"]
                        propertyChange.reason = change["변동사유"]
                        propertyChange.period = change["기간"]
                        propertyChange.insert(cur)
                        pp.updatePrice(cur, detail["현재가액"], propertyID)
                        con.commit()

                else:
                    result = pp.selectOne(cursor= cur, \
                                          detail= change["재산명세"], \
                                          politicianID = politicianID, \
                                          propertyListID = propertyListID, \
                                          price = change["현재가액"]
                                          )
                    if(result != None):
                        propertyID = result[0]
                    else:
                        print(politician["국회의원 이름"] + section + kind + relation +"Property ID 검색오류")
                        # 없으면 삽입시도 하는게 코드 효율 높을 수도 있지만, 어차피 1년에 한번에 실행인데 굳이
                        continue
                    propertyChange.propertyID = propertyID
                    # 그냥 감소액 등 넣는거 고려
                    propertyChange.price = change["현재가액"]
                    propertyChange.reason = change["변동사유"]
                    propertyChange.period = change["기간"]
                    propertyChange.insert(cur)
                    pp.updatePrice(cur, change["현재가액"], propertyID)
                    con.commit()

        con.close()


    def parsePropertyList(self, parsedJson):


        con, cur = self.dbConnect()
        propertyListCategory = []

        # print("stub")

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
        # dbinfoDir = "E:\work\Frankly\pdfParser\InformationClass/dbinfo.info"
        # dbinfoDir = "D:\code\Frankly\pdfParser\InformationClass/dbinfo.info"
        dbinfoDir = "/home/hanpaa/IdeaProjects/Frankly/pdfParser/dbinfo.info"
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


# option = sys.argv[1]
#
#
# if option == '1':
#     pe = PropertyExtract()
#     pe.jsonParse()