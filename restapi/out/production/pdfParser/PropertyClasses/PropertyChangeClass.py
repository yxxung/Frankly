class PropertyChange:
    __totalIncrease = 0;
    __totalDecrease = 0;
    __presentValue = 0;
    __previousValue = 0
    __reason = None

    def __init__(self, preValue, nowValue, increase, decrease):
        self.__previousValue = preValue
        self.__presentValue = nowValue
        self.__totalIncrease = increase
        self.__totalDecrease = decrease


    def getPreviousValue(self):
        return self.__previousValue

    def setPreviousValue(self, preValue):
        self.__previousValue = preValue

    def getPresentValue(self):
        return self.__presentValue

    def setPresentValue(self, nowValue):
        self.__presentValue = nowValue

    def getTotalIncrease(self):
        return self.__totalIncrease

    def setTotalIncrease(self, increase):
        self.__totalIncrease = increase

    def getTotalDecresase(self):
        return self.__totalDecrease

    def setTotalDecrease(self,decrease):
        self.__totalDecrease = decrease

    def getReason(self):
        return self.__reason

    def setReason(self, reason):
        self.__reason
