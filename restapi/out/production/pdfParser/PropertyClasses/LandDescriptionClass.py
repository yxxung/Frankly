# -*- coding: utf-8 -*-
from PropertyChangeClass import *


class LandDescriptionClass(PropertyChange):
    __kinds = None
    __details = None

    def __init__(self, preValue, nowValue, increase, decrease):
        super().__init__(preValue, nowValue, increase, decrease)
        self.kinds = "본인"

    def setDetails(self, details):
        self.__details = details

    def getDetails(self):
        return self.__details
