class Politician:
    __name = None
    __belong = None
    __position = None
    __Land = None
    __RealEstate = None
    __RealRight = None
    __Deposit = None
    __PoliticDeposit = None
    __Debt = None

    def __init__(self, name, belong, position):
        self.__name = name
        self.__belong = belong
        self.__position = position


    def setLand(self, Land):
        self.__Land = Land

    def getLand(self):
        return self.__Land

