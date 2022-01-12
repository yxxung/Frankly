#-*- coding: utf-8 -*-

'''
@Author 최제현
@Date 21/1/8

'''
import traceback

from PropertyClasses.Parsers.PropertyMainParser import PropertyMainParser


def main():
    filePath = './parsed.txt'
    try:

        parser = PropertyMainParser(filePath)
        parser.parse()

    except Exception as e:
        traceback.print_exc()
        exit(99)



if __name__ == '__main__':
    main()
