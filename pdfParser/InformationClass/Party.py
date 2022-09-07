

class Party:


    def __init__(self, partyName):
        self._partyID = 0
        self._partyName = partyName

    @property
    def partyID(self):
        return self._partyID

    @partyID.setter
    def partyID(self,partyID):
        self._partyID = partyID

    @property
    def partyName(self):
        return self._partyName

    @partyName.setter
    def partyName(self, partyName):
        self._partyName = partyName


    # 이름비교
    def __eq__(self, other):
        return self.partyName == other

    def __hash__(self):
        return self.partyName

    def insert(self, cursor):
        sql = "INSERT INTO Party VALUES('" + str(self.partyID) +"','" + self.partyName + "')"
        cursor.execute(sql)


