class Property:

    @property
    def assetID(self):
        return self._assetID
    @assetID.setter
    def assetID(self, assetID):
        self.assetID = assetID

    @property
    def propertyListID(self):
        return self._propertyListID

    @propertyListID.setter
    def propertyListID(self, propertyListID):
        self._propertyListID = propertyListID

    @property
    def politicianID(self):
        return self._politicianID

    @politicianID.setter
    def politicianID(self, politicianID):
        self._politicianID = politicianID

    @property
    def presentPrice(self):
        return self._presentPrice

    @presentPrice.setter
    def presentPrice(self, presentPrice):
        self._presentPrice = presentPrice