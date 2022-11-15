#-*- coding: utf-8 -*-

'''
@Author 최제현
@Date 21/1/8

국회공보 주소

https://www.assembly.go.kr/portal/bbs/B0000059/list.do?pageIndex=1&menuNo=600103&searchWrdMb=&searchDtGbnMb=c0&pageUnit=10&searchDtGbn=c0&sdate=&edate=&cl1Cd=&searchCnd=1&searchWrd=%EC%9E%AC%EC%82%B0

정치인 재산 정보를 pdf에서 파싱하여, json으로 변환

'''
import gc
import traceback
import os

from PropertyClasses.Parsers.PropertyMainParser import PropertyMainParser

class PropertyTXTFileParser:
    def propertyTXTParse(self, filePath):
        # filePath = 'E:\work\Frankly\pdfParser\PropertyClasses\Parsers\moneyTXT'
        # filePath = 'moneyTXT'
        # filePath = 'D:\code\Frankly\pdfParser\PropertyClasses\moneyTXT'
        fileList = os.listdir(filePath)
        pdfPath = filePath + "/"

        for filename in fileList:
            try:
                if (filename.endswith(".txt")):
                    print(filename + " start\n")
                    parser = PropertyMainParser(pdfPath+filename)
                    parser.parse()
                    parser = None

            except Exception as e:
                traceback.print_exc()
                print(filename)
                exit(99)

