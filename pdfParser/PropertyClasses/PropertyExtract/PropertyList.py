class PropertyList:

    @property
    def propertyListID(self):
        return self._propertyListID

    @propertyListID.setter
    def propertyListID(self, propertyListID):
        self._propertyListID = propertyListID

    @property
    def propertyListName(self):
        return self._propertyListName

    @propertyListName.setter
    def propertyListName(self, propertyListName):
        self._propertyListName = propertyListName

    @property
    def relation(self):
        return self._relation

    @relation.setter
    def relation(self, relation):
        self._relation = relation

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, kind):
        self._kind = kind

    @property
    def propertyDetail(self):
        return self._propertyDetail

    @propertyDetail.setter
    def propertyDetail(self, propertyDetail):
        self._propertyDetail = propertyDetail