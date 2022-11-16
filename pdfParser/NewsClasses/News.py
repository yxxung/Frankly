
"""

https://developers.naver.com/docs/serviceapi/search/news/news.md#%EB%89%B4%EC%8A%A4

@params
query	string	Y	-	검색을 원하는 문자열로서 UTF-8로 인코딩한다.
display	integer	N	10(기본값), 100(최대)	검색 결과 출력 건수 지정
start	integer	N	1(기본값), 1000(최대)	검색 시작 위치로 최대 1000까지 가능
sort	string	N	sim, date(기본값)	정렬 옵션: sim (유사도순), date (날짜순)
"""


import traceback
import pymysql
import os
import sys
import urllib.request
import json
import datetime
import requests
import re
from time import sleep


from string import whitespace

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


from InformationClass.openAPI import openAPI
from InformationClass.Politician import Politician


class News:

    def __init__(self):
        self.newsID = None
        self.politicianID = None
        self.newsTitle = None
        self.newsURL = None
        # self.newsKeyword = None
        self.newsAbstract = None

    @property
    def newsID(self):
        return self._newsID

    @newsID.setter
    def newsID(self, newsID):
        self._newsID = newsID

    @property
    def politicianID(self):
        return self._politicianID

    @politicianID.setter
    def politicianID(self, politicianID):
        self._politicianID = politicianID

    @property
    def newsTitle(self):
        return self._newsTitle

    @newsTitle.setter
    def newsTitle(self, newsTitle):
        self._newsTitle = newsTitle

    @property
    def newsURL(self):
        return self._newsURL

    @newsURL.setter
    def newsURL(self, newsURL):
        self._newsURL = newsURL

    # @property
    # def newsKeyword(self):
    #     return self._newsKeyword
    #
    # @newsKeyword.setter
    # def newsKeyword(self, newsKeyword):
    #     self._newsKeyword = newsKeyword

    @property
    def newsAbstract(self):
        return self._newsAbstract

    @newsAbstract.setter
    def newsAbstract(self, newsAbstract):
        self._newsAbstract = newsAbstract

    @property
    def newsDate(self):
        return self._newsDate

    @newsDate.setter
    def newsDate(self, newsDate):
        self._newsDate = newsDate

    @property
    def newsContent(self):
        return self._newsContent

    @newsContent.setter
    def newsContent(self, newsContent):
        self._newsContent = newsContent

# ------------------------------------------------------------

    def insert(self, cursor):
        try:
            sql = "INSERT INTO News VALUE (%s,%s, %s, %s,%s, %s, '')"
            cursor.execute(sql,(None,self.politicianID, self.newsTitle, self.newsURL, self.newsAbstract, self.newsDate))
            return True
        except pymysql.err.IntegrityError as e:
            code, msg = e.args
            print("뉴스정보 중복")
            sql = "SELECT count(NewsID) from News"
            cursor.execute(sql)
            selectcount = cursor.fetchone()
            sql = "ALTER TABLE News AUTO_INCREMENT = %s"
            cursor.execute(sql,(selectcount[0]))
            print("auto increment set : " + str(selectcount[0]))
            raise Exception('News 중복')
        except Exception as e:
            traceback.print_exc()

    def update(self, cursor):
        try:
            sql = "UPDATE News SET newsContents = %s WHERE newsID = %s "
            cursor.execute(sql,(self.newsContent, self.newsID))

        except Exception as e:
            traceback.print_exc()


    def selectALL(self, cursor):

        sql = "SELECT * FROM News"
        cursor.execute(sql)
        selectNews = cursor.fetchall()
        NewsList = []

        for news in selectNews:
            n = News()
            n.newsID = news[0]
            n.politicianID = news[1]
            n.newsTitle = news[2]
            n.newsURL = news[3]
            # n.newsKeyword = news[4]
            n.newsAbstract = news[4]
            n.newsContent = news[5]
            n.newsContent = news[6]
            NewsList.append(n)

            return NewsList

    def selectByID(self, cursor, politicianID):

        sql = "SELECT * FROM News WHERE politicianID = %s AND newsContents = %s "
        cursor.execute(sql,(politicianID,''))
        selectNews = cursor.fetchall()
        NewsList = []

        for news in selectNews:
            n = News()
            n.newsID = news[0]
            n.politicianID = news[1]
            n.newsTitle = news[2]
            n.newsURL = news[3]
            n.newsAbstract = news[4]
            n.newsDate = news[5]
            n.newsContent = news[6]
            NewsList.append(n)

        return NewsList

    def selectByIDDate(self, cursor, politicianID, startdate, enddate):

        sql = "SELECT * FROM News WHERE politicianID = %s AND newsDate >= %s AND newsDate <= %s;"
        cursor.execute(sql,(politicianID, startdate, enddate))
        selectNews = cursor.fetchall()
        NewsList = []

        for news in selectNews:
            n = News()
            n.newsID = news[0]
            n.politicianID = news[1]
            n.newsTitle = news[2]
            n.newsURL = news[3]
            # n.newsKeyword = news[4]
            n.newsAbstract = news[4]
            n.newsDate = news[5]
            n.newsContent = news[6]
            NewsList.append(n)

        return NewsList

    def selectNewsDateList(self, cursor, targetDate):

        sql = "SELECT DATE_FORMAT(DATE_SUB(`newsDate`, INTERVAL (DAYOFWEEK(`newsDate`)-1) DAY), '%%Y-%%m-%%d') as start,\
                    DATE_FORMAT(DATE_SUB(`newsDate`, INTERVAL (DAYOFWEEK(`newsDate`)-7) DAY), '%%Y-%%m-%%d') as end,\
                    DATE_FORMAT(`newsDate`, '%%Y%%u') AS `date`\
                    FROM frankly.News\
                    WHERE newsDate > %s \
                    GROUP BY date;"

        cursor.execute(sql, targetDate)
        result = cursor.fetchall()

        return result

    #     -----------------------------------------
    # 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
    # 네이버 검색 Open API 예제 - 블로그 검색
    # targetDate foramt yyyy-mm-dd
    def getNewsFromAPI(self, targetDate):
        KST = datetime.timezone(datetime.timedelta(hours=9))
        targetDate = datetime.datetime.strptime(targetDate, "%Y-%m-%d").replace(tzinfo=KST)
        total = -1

        con, cur = self.dbConnect()
        api = openAPI()
        api.setAPIInfo(cur,"News")



        client_id = api.secretKey.split(" ")[0]
        client_secret = api.secretKey.split(" ")[1]

        p = Politician()
        politicianList = p.selectALL(cur)

        for politicain in politicianList:
            sleep(1)
            encText = urllib.parse.quote(politicain.politicianName + " 국회의원")

            startPage = 1
            display = 100
            url = api.URL + "?query="+ encText  + "&display=1&start="+ str(startPage) +"&sort=date"# json 결과
            # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과

            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id",client_id)
            request.add_header("X-Naver-Client-Secret",client_secret)
            try:
                response = urllib.request.urlopen(request)
                rescode = response.getcode()
                if(rescode==200):
                    response_body = response.read()
                    content = json.loads(response_body.decode('utf-8'))
                    total = content['total']
                else:
                    print("Error Code:" + str(rescode))
            except:
                rescode = -1
                time = 0
                while rescode == 200 or time == 50:
                    time = time + 1
                    sleep(10)
                    try:
                        response = urllib.request.urlopen(request)
                        rescode = response.getcode()
                        if(rescode==200):
                            response_body = response.read()
                            content = json.loads(response_body.decode('utf-8'))
                            total = content['total']
                            break
                    except:
                        exit(-1)

                """
                content
                rss	-	디버그를 쉽게 하고 RSS 리더기만으로 이용할 수 있게 하기 위해 만든 RSS 포맷의 컨테이너이며 그 외의 특별한 의미는 없다.
                channel	-	검색 결과를 포함하는 컨테이너이다. 이 안에 있는 title, link, description 등의 항목은 참고용으로 무시해도 무방하다.
                lastBuildDate	datetime	검색 결과를 생성한 시간이다.
                total	integer	검색 결과 문서의 총 개수를 의미한다.
                start	integer	검색 결과 문서 중, 문서의 시작점을 의미한다.
                display	integer	검색된 검색 결과의 개수이다.
                item/items	-	XML 포멧에서는 item 태그로, JSON 포멧에서는 items 속성으로 표현된다. 개별 검색 결과이며 title, originallink, link, description, pubDate를 포함한다.
                title	string	개별 검색 결과이며, title, originallink, link, description, pubDate 를 포함한다.
                originallink	string	검색 결과 문서의 제공 언론사 하이퍼텍스트 link를 나타낸다.
                link	string	검색 결과 문서의 제공 네이버 하이퍼텍스트 link를 나타낸다.
                description	string	검색 결과 문서의 내용을 요약한 패시지 정보이다. 문서 전체의 내용은 link를 따라가면 읽을 수 있다. 패시지에서 검색어와 일치하는 부분은 태그로 감싸져 있다.
                pubDate	datetime	검색 결과 문서가 네이버에 제공된 시간이다.
                """


            while(startPage < total):
                url = api.URL + "?query="+ encText  + "&display="+ str(display) +"&start="+ str(startPage) +"&sort=date"# json 결과
                # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과

                request = urllib.request.Request(url)
                request.add_header("X-Naver-Client-Id",client_id)
                request.add_header("X-Naver-Client-Secret",client_secret)

                try:
                    response = urllib.request.urlopen(request)
                    rescode = response.getcode()
                    if(rescode==200):
                        response_body = response.read()
                        content = json.loads(response_body.decode('utf-8'))
                    else:
                        print("Error Code:" + str(rescode))
                except:
                    rescode = -1
                    time = 0
                    while rescode == 200 or time == 50:
                        time = time + 1
                        sleep(10)
                        try:
                            response = urllib.request.urlopen(request)
                            rescode = response.getcode()
                            if(rescode==200):
                                response_body = response.read()
                            content = json.loads(response_body.decode('utf-8'))
                            break
                        except:
                            continue

                try:
                    for item in content["items"]:
                        if(item["link"].startswith("https://n.news.naver.com/")):
                            newNews = News()
                            newNews.newsURL = item["link"]
                            newNews.newsTitle = item['title'].replace("&quot;","").replace("<b>","").replace("&apos;", "")
                            newNews.newsDate = datetime.datetime.strptime(item['pubDate'], '%a, %d %b %Y %H:%M:%S %z')
                            newNews.newsAbstract = item['description']
                            newNews.politicianID = politicain.politicianID

                            if(newNews.newsDate < targetDate):
                                startPage = total
                                break

                            newNews.insert(cur)
                except:
                    con.commit()

                    # 'https://n.news.naver.com/mnews/article/088/0000774104?sid=100'
                    # xpath] /html/body/div/div[2]/div/div[1]/div[1]/div[2]
                    # selector] newsct_article
                    print(politicain.politicianName + " 뉴스 삽입완료")
                    break
                con.commit()

                    # 'https://n.news.naver.com/mnews/article/088/0000774104?sid=100'
                    # xpath] /html/body/div/div[2]/div/div[1]/div[1]/div[2]
                    # selector] newsct_article

                startPage = startPage + 100
                if(startPage == total):
                    print(politicain.politicianName + " 뉴스 삽입완료")
                    break
                elif(startPage > total):
                    display = startPage - total - 1
                    startPage = startPage - 100
                elif(startPage == 1001):
                    startPage = total
                    print(politicain.politicianName + " 뉴스 삽입완료")
                    break




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

    def newsCrawling(self):
        con, cur = self.dbConnect()
        politicianList = Politician().selectALL(cur)
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        emailPattern = re.compile(r'[a-zA-Z0-9_-]+@[a-z]+.[a-z]+')
        urlPattern = re.compile(r'(?:https?:\/\/)?[-_0-9a-z]+(?:\.[-_0-9a-z]+)+')
        whiteSpacePattern = re.compile(f'[{whitespace}]+')
        emojiPattern = re.compile('[^A-Za-z0-9가-힣 ,.\"\']')

        # selenium set
        # driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))


        for politician in politicianList:
        # 크롤링 테스트 이후 loop 걸어서 진행
            newsList = self.selectByID(cur, politician.politicianID)
            print(politician.politicianName+ " parsing..")
            for news in newsList:
                sleep(0.08)
                # driver.get(news.newsURL)
                # driver.implicitly_wait(3)
                response = requests.get(url=news.newsURL,headers=headers)
                bs = BeautifulSoup(response.text, "html.parser")
                divTag = None
                divTag = bs.find('div', {'class': 'go_trans _article_content'})

                if(divTag == None):
                    print(news.newsURL + " HTML 파싱 오류")
                    continue

                    # 본문 전처리

                newsContent = divTag.text.replace("\n", " ")

                newsContent = emailPattern.sub(repl='', string=newsContent)
                newsContent = urlPattern.sub(repl='', string=newsContent)
                newsContent = whiteSpacePattern.sub(repl=' ', string=newsContent)
                newsContent = emojiPattern.sub(repl='', string=newsContent)

                news.newsContent = newsContent

                try:
                    news.update(cur)
                    con.commit()
                except:
                    print("update error" + newsContent)
                    continue
        con.close()

# if __name__ == "__main__":
#     n = News()
#     n.getNewsFromAPI(targetDate="2022-10-01")
#     n.newsCrawling()