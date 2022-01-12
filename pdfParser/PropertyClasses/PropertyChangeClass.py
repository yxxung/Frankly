'''
@Author 최제현
@Date 21/1/8

'''


class PropertyChange:
    fileStartPos = 0
    fileEndPos = 0
    __totalIncrease = 0
    __totalDecrease = 0
    __presentValue = 0
    __previousValue = 0
    __reason = None

    def __init__(self, preValue, nowValue, increase, decrease):
        self.__previousValue = preValue
        self.__presentValue = nowValue
        self.__totalIncrease = increase
        self.__totalDecrease = decrease


    @property
    def getPreviousValue(self):
        return self.__previousValue

    @getPreviousValue.setter
    def setPreviousValue(self, preValue):
        self.__previousValue = preValue

    @property
    def getPresentValue(self):
        return self.__presentValue

    @getPresentValue.setter
    def setPresentValue(self, nowValue):
        self.__presentValue = nowValue

    @property
    def getTotalIncrease(self):
        return self.__totalIncrease

    @getTotalIncrease.setter
    def setTotalIncrease(self, increase):
        self.__totalIncrease = increase

    @property
    def getTotalDecresase(self):
        return self.__totalDecrease

    @getTotalDecresase.setter
    def setTotalDecrease(self,decrease):
        self.__totalDecrease = decrease

    @property
    def getReason(self):
        return self.__reason

    @getReason.setter
    def setReason(self, reason):
        self.__reason = reason

    @property
    def getFileStartPosition(self):
        return self.fileStartPos

    @getFileStartPosition.setter
    def setFileStartPosition(self, pos):
        self.fileStartPos = pos

    @property
    def getFileEndPoisition(self):
        return self.fileEndPos

    @getFileEndPoisition.setter
    def setFileEndPosition(self, pos):
        self.fileEndPos = pos
