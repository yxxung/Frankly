'''
@Author 최제현
@Date 21/1/8

'''

class MainParser:
    __file = None
    __filePos = 0;


    def __init__(self, file):
        self.__file = file

    def fileIterator(self):
        string = self.__file.readLine()

    def checkDivide(self, string):
        print()
