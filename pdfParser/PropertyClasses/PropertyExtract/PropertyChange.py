class PropertyChange:

    @property
    def changeID(self):
        return self._changeID

    @changeID.setter
    def changeID(self, changeID):
        self._changeID = changeID

    @property
    def politicianID(self):
        return self._politicianID

    @politicianID.setter
    def politicianID(self, politicianID):
        self._politicianID = politicianID

    @property
    def propertyListID(self):
        return self._propertyListID

    @propertyListID.setter
    def propertyListID(self, propertyListID):
        self._propertyListID = propertyListID

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, reason):
        self._reason = reason