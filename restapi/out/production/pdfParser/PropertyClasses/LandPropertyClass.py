# -*- coding: utf-8 -*-
from PropertyChangeClass import *


class LandProperty(PropertyChange):
    __DescriptionList = None

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
