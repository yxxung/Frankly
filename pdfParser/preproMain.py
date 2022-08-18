#-*- coding: utf-8 -*-

'''
@Author 최제현
@Date 21/1/8

'''
import gc
import traceback
import os

from PropertyClasses.Parsers.PropertyMainParser import PropertyMainParser


def main():
    filePath = './moneyTXT'
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



if __name__ == '__main__':
    main()
