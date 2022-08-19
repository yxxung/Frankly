from Politician import Politician
import sys
import json
import os

def parseJsonToPolitician():

    jsonParse()

def jsonParse():
    jsonDir = 'E:\work\Frankly\pdfParser\InformationClass\Json'
    fileList = os.listdir(jsonDir)
    politicianList = []

    fileName = "국회의원 지역번호.json"
    with open(fileName, encoding="UTF8") as jsonObject:
        districtNumber = json.load(jsonObject)

    for fileName in fileList:
        with open(jsonDir+"/"+fileName, encoding="UTF8") as jsonObject:
            parsedJson = json.load(jsonObject)
            print("stub")
            for index in range(len(parsedJson)-1):


                jsonIndex = index+1
                politician = Politician(jsonIndex)
                politician.politicianName = parsedJson[jsonIndex]['HG_NM']
                politician.hanName = parsedJson[jsonIndex]['HJ_NM']
                politician.engName = parsedJson[jsonIndex]['ENG_NM']
                politician.lunar = parsedJson[jsonIndex]['BTH_GBN_NM']
                politician.partyID =  parsedJson[jsonIndex]['BTH_DATE']
                politician.regionID =  parsedJson[jsonIndex]['ORIG_NM']
                politician.selectNumber =  parsedJson[jsonIndex]['REELE_GBN_NM']
                politician.selectInfo =  parsedJson[jsonIndex]['UNITS']
                politician.sex =  parsedJson[jsonIndex]['SEX_GBN_NM']
                politician.contact =  parsedJson[jsonIndex]['TEL_NO']
                politician.email =  parsedJson[jsonIndex]['E_MAIL']
                politician.homePage =  parsedJson[jsonIndex]['HOMEPAGE']
                politician.aide =  parsedJson[jsonIndex]['STAFF']
                politician.secretary =  parsedJson[jsonIndex]['SECRETARY']
                politician.personalAssistant =  parsedJson[jsonIndex]['SECRETARY2']
                politicianList.append(politician)
            print("stub")



option = sys.argv[1]
if option == '1':
    parseJsonToPolitician()



