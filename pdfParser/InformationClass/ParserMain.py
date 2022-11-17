'''
@Author 최제현
@Date 22/8/

국회공보 주소

https://www.assembly.go.kr/portal/bbs/B0000059/list.do?pageIndex=1&menuNo=600103&searchWrdMb=&searchDtGbnMb=c0&pageUnit=10&searchDtGbn=c0&sdate=&edate=&cl1Cd=&searchCnd=1&searchWrd=%EC%9E%AC%EC%82%B0

정치인, 정당, 지역 정보를 DB에 저장.

'''
import re

import pdfplumber
import pymysql
# 파일이름, class명
from InformationClass.ConferenceAttendance import Attendance
from InformationClass.ConferenceSchedule import ConferenceSchedule
from InformationClass.openAPI import openAPI
from InformationClass.Politician import Politician
from InformationClass.Region import Region
from InformationClass.Party import Party
from datetime import datetime
import traceback


import sys
import json
import os
import requests
import pprint

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

    def parseAttendancePDF(self, pdfDir):
        # pdfDir = 'E:\work\Frankly\pdfParser\InformationClass\Json'
        # pdfDir = 'D:\code\Frankly\pdfParser\InformationClass/attendance'
        fileList = os.listdir(pdfDir)

        table_settings = {
            "vertical_strategy" : "lines",
            "horizontal_strategy" : "lines",
            # "snap_tolerance": 1,
            # "snap_x_tolerance": 1,
            # "snap_y_tolerance": 1,
            # "join_tolerance": 1,
            # "join_x_tolerance": 1,
            # "join_y_tolerance": 1,
            # "edge_min_length": 1,
            # "min_words_vertical": 1,
            # "min_words_horizontal": 1,
            # "keep_blank_chars": False,
            # "text_tolerance": 1,
            # "text_x_tolerance": 1,
            # "text_y_tolerance": 1,
            # "intersection_tolerance": 1,
            # "intersection_x_tolerance": 1,
            # "intersection_y_tolerance": 1
        }

        for fileName in fileList:
            if(fileName.endswith(".pdf")):
                with pdfplumber.open(pdfDir + "/" + fileName) as pdf:
                    txtName = pdfDir+ "/" + fileName.replace(".pdf","") + ".txt"
                    page = pdf.pages[1]
                    im = page.to_image(resolution=150)
                    im.reset().debug_tablefinder(table_settings).save("./debug.PNG", format="PNG")
                    f = open(txtName,'w', encoding="UTF-8")
                    for pdf_page in pdf.pages:
                        try:
                            table = pdf_page.extract_table(table_settings)
                            str1 = ['|'.join(list(filter(None, line))) for line in table]
                            str2 = [str.replace("\n"," ") for str in str1]
                            str3 = '\n'.join(str2)
                            f.write(str3+'\n')
                            # f.write(str3)
                        except Exception as e:
                            print(e)

    def parseAttendance(self):
        con, cur = self.dbConnect()
        # pdfDir = 'E:\work\Frankly\pdfParser\InformationClass\Json'
        pdfDir = 'D:\code\Frankly\pdfParser\InformationClass/attendance'
        pdfDir = ''
        fileList = os.listdir(pdfDir)
        for fileName in fileList:
            if(fileName.endswith(".txt")):
                with open(pdfDir + "/" + fileName, encoding="UTF8") as file:
                    print(fileName)

                    string = file.readline()
                    token = string.split("|")
                    if(token[0] == "구분"):
                        conferenceNumber = token[1].replace("\n", "")

                    else:
                        print( fileName + " file error")

                    # 차수 계산
                    string = file.readline()
                    token = string.split("|")
                    if(token[0] == "의원명"):
                        attendanceLength = len(token) - 8
                    else:
                        print( fileName + " file error")

                    # 날짜 리스트 추출

                    dateList = []
                    conferenceIDList = []

                    string = file.readline()
                    token = string.split("|")
                    index = 0
                    if(token[0].startswith("(") and attendanceLength == len(token)):
                        conference = ConferenceSchedule()
                        for date in token:
                            index += 1
                            # 정규표현식으로 숫자들 추출 date 패턴으로 변경
                            number = re.findall('\d+', date)
                            fixedDate = number[0] + "-" + number[1] + "-" + number[2]
                            result = conference.search(cur, fixedDate, "conferenceDate")
                            if(result != None):
                                conferenceID = result[0]
                            else:
                                print(token[0] + fixedDate + " 회의정보누락 " + fileName )
                                newSchedule = ConferenceSchedule()
                                newSchedule.conferenceDate = fixedDate
                                newSchedule.conferenceTitle = fileName.split()[0].replace("(", "국회(").replace("임", "임시회")
                                newSchedule.generation = conference.search(cur, newSchedule.conferenceTitle, "conferenceTitle")[1]
                                newSchedule.conferenceSession = index
                                newSchedule.insert(cur)
                                con.commit()
                                print(newSchedule.conferenceDate + "삽입")
                                result = conference.search(cur, fixedDate, "conferenceDate")
                                conferenceID = result[0]

                            dateList.append(fixedDate)
                            conferenceIDList.append(conferenceID)
                    else:
                        print( fileName + " file error")



                    pp = Politician()
                    statement = True
                    while statement:
                        string = file.readline()

                        if(string == ''):
                            statement = False
                            continue

                        token = string.split("|")
                        # 페이지 변경
                        if(token[0] == "구분"):
                            string = file.readline()
                            string = file.readline()
                            string = file.readline()
                            token = string.split("|")

                        if(string == ''):
                            statement = False
                            continue
                        # 국회의원 ID 검색
                        ppName = token[0].split("(")
                        if(len(ppName) == 2 and ppName[1] == "비)"):
                            result = pp.selectNameID(cursor= cur,\
                                                     input = ppName[0],\
                                                     column="142")
                        else:
                            if(ppName[0] == "이수진" or ppName[0] == "김병욱"):
                                input = [ppName[0], token[1]]
                                result = pp.selectNameID(cursor= cur,\
                                                input= input,\
                                                column= "politicianName")

                        if(len(result) != 0):
                            politicianID = result[0][0]
                            if(len(result) == 2):
                                for politicianSelectResult in result:
                                    # 같은 당 동명이인중 비례대표일 경우(비) 라고 표기는 되지만, 검색은 됨.
                                    if(politicianSelectResult[1] != 142):
                                        politicianID = politicianSelectResult[0]


                        else:
                            print(token[0] + " 사퇴")
                            continue

                        attendanceList = []

                        for index in range(attendanceLength):
                            # 국회의원 임명 전 처리
                            if(token[index+2]=="-"):
                                continue
                            attendance = Attendance()

                            attendance.conferenceID = conferenceIDList[index]
                            # attendance.conferenceDate = dateList[index]
                            attendance.politicianID = politicianID
                            attendance.attendanceCheck(token, index)
                            attendanceList.append(attendance)

    #                    출석 카운트 맞는지 체크
                        self.attendanceVaildateCheck(attendanceList, token)

                        for attendance in attendanceList:
                            try:
                                attendance.insert(cursor=cur)
                                con.commit()
                            except Exception as e:
                                print("출석정보 중복. 더 이상 삽입이 필요없거나 데이터 확인이 필요합니다.")
                                return



        con.close()




    def attendanceVaildateCheck(self, attendanceList, token):
        # token 순서 예시  강기윤|국민의힘|결석|출석|2|1|1|0|0|0
        attendanceCount = 0
        petitionLeave = 0
        businessTrip = 0
        absence = 0
        for attendance in attendanceList:
            if(attendance.attendance == True):
                attendanceCount += 1
            elif(attendance.petitionLeave == True):
                petitionLeave += 1
            elif(attendance.businessTrip == True):
                businessTrip += 1
            else:
                absence += 1

        result = attendanceCount + petitionLeave + businessTrip + absence

        # 뒤에서부터 탐색
        if(attendanceCount == int(token[len(token)-5]) and\
                petitionLeave == int(token[len(token)-3]) and\
                businessTrip == int(token[len(token)-2]) and\
                result == int(token[len(token)-6])):
            # print(str(token[0]) + "출석 OK")
            return True
        else:
            print(str(token[0]) + "출석 집계 에러")
            return False




    def jsonParse(self):

        jsonDir = 'E:\work\Frankly\pdfParser\InformationClass\Json'
        fileList = os.listdir(jsonDir)

        for fileName in fileList:
            with open(jsonDir+"/"+fileName, encoding="UTF8") as jsonObject:
                parsedJson = json.load(jsonObject)

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

    def getScheduleFromAPI(self):
        con, cur = self.dbConnect()
        api = openAPI()
        api.setAPIInfo(cur, "conferenceschedule")

        # json 데이터 이상.. 2002년 데이터도 들어가있음 걸러내야함.
        params = {'Key': api.secretKey, 'Type': 'json',\
                  'pIndex': 1, 'pSize' : 92, 'UNIT_CD' : '100021'}
        response = requests.get(api.scheduleURL, params=params)
        contents = response.text

        scheduleJson = json.loads(contents)
        pattern = r'[^0-9]'
        try:
            for parsedJson in scheduleJson['nekcaiymatialqlxr'][1]["row"]:
                schedule = ConferenceSchedule()
                schedule.generation = re.sub(pattern,'',parsedJson["UNIT_NM"])
                schedule.conferenceTitle = parsedJson['MEETINGSESSION']
                schedule.conferenceDate = parsedJson['MEETTING_DATE']
                schedule.conferenceSession = re.sub(pattern,'',parsedJson['CHA'])
                schedule.insert(cursor=cur)
            con.commit()
            con.close()
        except Exception as e:
            exit(0)



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
# parser = ParserMain()
#
#
# if option == '1':
#
#     parser.parseJsonToPolitician()
#
# elif option == '2':
#     parser.parseAttendancePDF()
#     parser.parseAttendance()
#
# elif option == '3':
#     parser.getScheduleFromAPI()


