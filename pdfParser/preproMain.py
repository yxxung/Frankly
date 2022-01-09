#-*- coding: utf-8 -*-

'''
@Author 최제현
@Date 21/1/8

'''
from PropertyClasses.MainParser import MainParser


def main():
    filePath = './parsed.txt'
    try:

        parser = MainParser(filePath)
        parser.parse()

    except Exception as e:
        print(e)
        exit(99)



if __name__ == '__main__':
    main()
