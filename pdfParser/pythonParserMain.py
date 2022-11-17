from InformationClass.ParserMain import ParserMain
from NewsClasses.News import News
from NewsClasses.KeywordExtract import KeywordExtract
from PropertyClasses.Parsers.propertyPDFParser import PropertyPDFParser
from PropertyClasses.Parsers.PropertyTXTFileParser import PropertyTXTFileParser
from PropertyClasses.PropertyExtract.PropertyExtract import PropertyExtract
import os

state = True

while(state):
    print("원하는 작업을 고르세요 번호만 입력하세요.")
    print("1 : 의회 일정 정보 수집")
    print("2 : 정치인 출석 정보 수집")
    print("3 : 정치인 뉴스 기사 및 키워드 수집")
    # print("4 : 정치인 뉴스 키워드 수집")
    print("4 : 정치인 재산 정보 수집")
    print("5 : 나가기")
    print("input : ")
    select = input()

    dir = "/home/hanpaa/IdeaProjects/Frankly/pdfParser"
    # dir = 'E:/work/Frankly/pdfParser'
    if(select == "1"):
        print("데이터가 이미 최신이면 자동종료됨.")
        # PoliticianInformationParser = ParserMain()
        # PoliticianInformationParser.getScheduleFromAPI()
    elif(select == "2"):
        pdfDir = dir + "/InformationClass/attendancePDF"
        PoliticianInformationParser = ParserMain()
        fileList = os.listdir(pdfDir)
        print("이 파일들이 맞는지 확인. 취소는 CTRL + C")

        for fileName in fileList:
            if(fileName.endswith(".pdf")):
                print(fileName)

        input("\t Press Enter Key to Continue")
        PoliticianInformationParser.parseAttendancePDF(pdfDir)
        # PoliticianInformationParser.parseAttendance()
    elif(select == "3"):
        news = News()
        print("연 월 일을 입력하면 해당 날짜 이후의 뉴스데이터를 수집합니다. 예) 2020 10 01 순으로 입력")
        print("년 : ")
        year = input()
        print("월 : ")
        month = input()
        print("일 : ")
        day = input()
        targetDate = year + "-" + month + "-" + day
        print(targetDate)
        # news.getNewsFromAPI(targetDate=targetDate)
        # news.newsCrawling()
        # KeywordExtract.keywordExtract(date=targetDate)
    # elif(select == "4"):
    #     print("뉴스 키워드 추출 뉴스 데이터 수집과 같은 월로 ")

    elif(select == "4"):
        pdfDir = dir + "/PropertyClasses/Parsers/moneyPDF"
        txtDir = dir + "/PropertyClasses/Parsers/moneyTXT"
        fileList = os.listdir(pdfDir)
        print("이 파일들이 맞는지 확인. 취소는 CTRL + C")

        for fileName in fileList:
            print(fileName)

        input("\t Press Enter Key to Continue")
        # PropertyPDFParser = PropertyPDFParser()
        # PropertyPDFParser.propertyPDFParse(pdfDir, txtDir)
        # PropertyTXTFileParser = PropertyTXTFileParser()
        # PropertyTXTFileParser.propertyTXTParse(txtDir)
        # PropertyExtract.jsonParse()

    elif(select == "5"):
        exit(0)

    else:
        print("wrong input")
        exit(-1)
