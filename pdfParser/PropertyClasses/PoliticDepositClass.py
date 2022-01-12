'''
@Author 최제현
@Date 21/1/12

'''
# -*- coding: utf-8 -*-
from PropertyClasses.PropertyChangeClass import PropertyChange


class PoliticDeposit(PropertyChange):
    __DescriptionList = None
    __error = 0

    def __init__(self, increase, decrease, preValue, nowValue):
        super().__init__(preValue, nowValue, increase, decrease)
        self.__DescriptionList = []

    def appendDescription(self, Description):
        self.__DescriptionList.append(Description)

    def deleteDescription(self, position):
        if len(self.__DescriptionList) == 0:
            return
        else:
            del self.__DescriptionList[position]


    def error(self):
        self.__error = 1
