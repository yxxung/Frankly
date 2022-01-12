#-*- coding: utf-8 -*-

'''
@Author 최제현
@Date 21/1/8

'''
from PropertyClasses.PropertyMainParser import PropertyMainParser


def main():
    filePath = './parsed.txt'
    try:

        parser = PropertyMainParser(filePath)
        parser.parse()

    except Exception as e:
        print(e)
        exit(99)



if __name__ == '__main__':
    main()
