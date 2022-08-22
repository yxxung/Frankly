class Region:

    def __init__(self, regionName):
        self._regionID = 0
        self._regionName = regionName


    @property
    def regionID(self):
        return self._regionID

    @regionID.setter
    def regionID(self, regionID):
        self._regionID = regionID

    @property
    def regionName(self):
        return self._regionName

    @regionName.setter
    def regionName(self, regionName):
        self._regionName = regionName

    # 이름비교
    def __eq__(self, other):
        return self.regionName == other

    def __hash__(self):
        return hash(self.regionName)

    def insert(self, cursor):
        sql = "INSERT INTO Region VALUES('" + str(self.regionID) +"','" + self.regionName + "')"
        cursor.execute(sql)