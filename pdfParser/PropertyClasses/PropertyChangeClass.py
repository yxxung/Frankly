'''
@Author 최제현
@Date 21/1/8

'''


class PropertyChange:
    # 단위액
    plusNum = ",000"
    fileStartPos = 0
    fileEndPos = 0
    __totalIncrease = 0
    __totalDecrease = 0
    __presentValue = 0
    __previousValue = 0
    __reason = None

    def __init__(self):
        self.__previousValue = None
        self.__presentValue = None
        self.__totalIncrease = None
        self.__totalDecrease = None


    @property
    def getPreviousValue(self):
        if self.__previousValue != None:
            return self.__previousValue
        else:
            return "NaN"

    @getPreviousValue.setter
    def setPreviousValue(self, preValue):
        if preValue != '0':
            self.__previousValue = preValue + self.plusNum
        elif preValue == '0':
            self.__previousValue = preValue
        else:
            print(self.fileStartPos + "error")

    @property
    def getPresentValue(self):
        if self.__presentValue != None:
            return self.__presentValue
        else:
            return "NaN"

    @getPresentValue.setter
    def setPresentValue(self, nowValue):
        if nowValue != '0':
            self.__presentValue = nowValue + self.plusNum
        elif nowValue == '0':
            self.__presentValue= nowValue
        else:
            print(self.fileStartPos + "error")

    @property
    def getTotalIncrease(self):
        if self.__totalIncrease != None:
            return self.__totalIncrease
        else:
            return "NaN"

    @getTotalIncrease.setter
    def setTotalIncrease(self, increase):
        if increase != '0':
            self.__totalIncrease = increase + self.plusNum
        elif increase == '0':
            self.__totalIncrease = increase
        else:
            print(self.fileStartPos + "error")

    @property
    def getTotalDecresase(self):
        if self.__totalDecrease != None:
            return self.__totalDecrease
        else:
            return "NaN"

    @getTotalDecresase.setter
    def setTotalDecrease(self,decrease):
        if decrease != '0':
            self.__totalDecrease = decrease + self.plusNum
        elif decrease == '0':
            self.__totalDecrease = decrease
        else:
            print(self.fileStartPos + "error")

    @property
    def getReason(self):
        if self.__reason != None:
            return self.__reason
        else:
            return "NaN"

    @getReason.setter
    def setReason(self, reason):
        self.__reason = reason

    @property
    def getFileStartPosition(self):
        if self.fileStartPos != None:
            return self.fileStartPos
        else:
            return "NaN"

    @getFileStartPosition.setter
    def setFileStartPosition(self, pos):
        self.fileStartPos = pos

    @property
    def getFileEndPoisition(self):
        if self.fileEndPos != None:
            return self.fileEndPos
        else:
            return "NaN"
    @getFileEndPoisition.setter
    def setFileEndPosition(self, pos):
        self.fileEndPos = pos
