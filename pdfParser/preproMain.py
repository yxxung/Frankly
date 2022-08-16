#-*- coding: utf-8 -*-

'''
@Author 최제현
@Date 21/1/8

'''
import traceback
import os

from PropertyClasses.Parsers.PropertyMainParser import PropertyMainParser


def main():
    filePath = './moneyTXT'
    fileList = os.listdir(filePath)
    pdfPath = filePath + "/"

    for filename in fileList:
        try:
            parser = PropertyMainParser(pdfPath+filename)
            parser.parse()

        except Exception as e:
            traceback.print_exc()
            print(filename)
            exit(99)



if __name__ == '__main__':
    main()
